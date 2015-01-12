# -*- coding: utf-8 -*-
"""Provides advertiser object.

Python library for interacting with the T1 API. Uses third-party module Requests
(http://docs.python-requests.org/en/latest/) to get and post data, and ElementTree
to parse it.
"""

from __future__ import absolute_import
from .t1object import T1Object

class T1Advertiser(T1Object):
	"""docstring for T1Advertiser"""
	collection = 'advertisers'
	type = 'advertiser'
	_relations = {
		'ad_server', 'agency', 'billing_contact', 'sales_contact', 'vertical',
	}
	_pull = {
		'ad_server_fee': float,
		'ad_server_id': int,
		'ad_server_password': None,
		'ad_server_username': None,
		'agency_id': int,
		'allow_x_strat_optimization': T1Object._int_to_bool,
		'billing_contact_id': int,
		'created_on': T1Object._strpt,
		'domain': None,
		'id': int,
		'minimize_multi_ads': T1Object._int_to_bool,
		'name': None,
		'sales_contact_id': int,
		'status': T1Object._int_to_bool,
		'updated_on': T1Object._strpt,
		'version': int,
		'vertical_id': int,
	}
	_push = _pull.copy()
	_push.update({
		'allow_x_strat_optimization': int,
		'minimize_multi_ads': int,
		'status': int,
	})
	_readonly = T1Object._readonly.copy()
	def __init__(self, session, properties=None, **kwargs):
		super(T1Advertiser, self).__init__(session, properties, **kwargs)
