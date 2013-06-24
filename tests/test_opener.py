#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (c) 2013 Qin Xuye <qin@qinxuye.me>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Created on 2013-5-17

@author: Chine
'''
import unittest

from cola.core.opener import BuiltinOpener, MechanizeOpener, GhostOpener

class Test(unittest.TestCase):


    def testBuiltinOpener(self):
        opener = BuiltinOpener()
        assert 'baidu' in opener.open('http://www.baidu.com')
         
    def testMechanizeOpener(self):
        test_url = 'http://www.baidu.com'
        opener = MechanizeOpener()
         
        assert 'baidu' in opener.open(test_url)
         
        br = opener.browse_open(test_url)
        assert u'百度' in br.title()
        assert 'baidu' in br.response().read()
        
    def testGhostOpener(self):
        from cola.core.extractor.preprocess import PreProcessor
        
        opener = GhostOpener()
        
        ghost = opener.ghost_open(
            'http://s.weibo.com/weibo/%25E8%25B6%2585%25E7%25BA%25A7%25E6%259C%2588%25E4%25BA%25AE?topnav=1&wvr=5&Refer=top_hot')
        ghost.wait_for_selector('div#pl_weibo_feedlist')
        html = ghost.content
        _, content = PreProcessor(html).process()
        self.assertIn(u'超级月亮', unicode(content))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()