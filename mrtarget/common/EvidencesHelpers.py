import json
import os
import random
import logging
import gzip

import functools
import itertools
import uuid
from abc import abstractmethod

import addict
import more_itertools

from mrtarget.common import URLZSource
from mrtarget.common.DataStructure import JSONSerializable
from mrtarget.common.ElasticsearchLoader import Loader
from mrtarget.common.LookupHelpers import LookUpDataRetriever, LookUpDataType
from mrtarget.common.connection import new_es_client

_l = logging.getLogger(__name__)


def make_lookup_data(es_client, redis_client):
    return LookUpDataRetriever(es_client,
                        redis_client,
                        data_types=(
                            LookUpDataType.TARGET,
                            LookUpDataType.DISEASE,
                            LookUpDataType.EFO,
                            LookUpDataType.ECO,
                            LookUpDataType.HPO,
                            LookUpDataType.MP
                        ),
                        autoload=True,
                        ).lookup


class ProcessContext(object):
    def __init__(self, **kwargs):
        self.kwargs = addict.Dict(kwargs)
        self.logger = logging.getLogger(__name__ + '_' + str(os.getpid()))

    @abstractmethod
    def put(self, line, **kwargs):
        pass

    def __del__(self):
        pass


class ProcessContextFileWriter(ProcessContext):
    def __init__(self, **kwargs):
        super(ProcessContextFileWriter, self).__init__(kwargs)
        self.logger.debug("called output_stream from %s", str(os.getpid()))

        valids_file_name = 'evidences_' + uuid.uuid4().hex + '.json.gz'
        valids_file_handle = to_source_for_writing(valids_file_name)
        self.kwargs.valids_file_name = valids_file_name
        self.kwargs.valids_file_handle = valids_file_handle

        invalids_file_name = 'validations_' + uuid.uuid4().hex + '.json.gz'
        invalids_file_handle = to_source_for_writing(invalids_file_name)
        self.kwargs.invalids_file_name = invalids_file_name
        self.kwargs.invalids_file_handle = invalids_file_handle

    def put(self, line, **kwargs):
        pass

    def __del__(self):
        super(ProcessContextFileWriter, self).__del__()
        self.logger.debug('closing files %s %s',
                          self.kwargs.valids_file_name,
                          self.kwargs.invalids_file_name)
        self.kwargs.valids_file_handle.close()
        self.kwargs.invalids_file_handle.close()


class ProcessContextESWriter(ProcessContext):
    def __init__(self, **kwargs):
        super(ProcessContextESWriter, self).__init__(kwargs)
        self.logger.debug("called output_stream from %s", str(os.getpid()))

        self.kwargs.es_client = new_es_client()
        self.kwargs.es_loader = Loader(es=self.kwargs.es_client, chunk_size=self.chunk_size)

    # TODO finish this method and integerate with the rest of the code
    def put(self, line, **kwargs):
        #     def put(self,
        #             index_name,
        #             doc_type,
        #             ID,
        #             body,
        #             create_index = True,
        #             operation= None,
        #             routing = None,
        #             parent = None,
        #             auto_optimise = False):
        self.kwargs.es_loader.put(body=line, **kwargs)

    def __del__(self):
        super(ProcessContextESWriter, self).__del__()
        self.kwargs.es_loader.flush()
        self.kwargs.es_loader.close()


def to_source_for_writing(filename):
    '''open a filename checking if .gz or not at the end of the filename'''
    return gzip.open(filename, mode='wb') \
            if filename.endswith('.gz') else open(filename, mode='w')


def from_source_for_reading(filename):
    '''return an iterator from izip (filename, (enumerate(file_handle))'''
    _l.debug('generate an iterator of (filename,enumerate) for filename %s', filename)
    it = more_itertools.with_iter(URLZSource(filename).open())
    return itertools.izip(itertools.cycle([filename]),enumerate(it, start=1))


def serialise_object_to_json(obj):
    serialised_obj = obj
    if not(isinstance(obj, str) or isinstance(obj, unicode)):
        if isinstance(obj, JSONSerializable):
            serialised_obj = obj.to_json()
        else:
            serialised_obj = json.dumps(obj)

    return serialised_obj


def reduce_tuple_with_sum(iterable):
    iterable
    return functools.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), iterable, (0, 0))


def make_validated_evs_obj(filename, hash, line, line_n, is_valid=False, explanation_type='', explanation_str='', target_id=None,
                           efo_id=None, data_type=None, id=None):
    return addict.Dict(is_valid=is_valid, explanation_type=explanation_type,
                       explanation_str=explanation_str, target_id=target_id,
                       efo_id=efo_id, data_type=data_type, id=id, line=line, line_n=line_n,
                       filename=filename, hash=hash)
