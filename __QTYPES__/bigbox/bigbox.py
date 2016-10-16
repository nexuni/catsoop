# This file is part of CAT-SOOP
# Copyright (c) 2011-2016 Adam Hartz <hartz@mit.edu>

# This program is free software: you can redistribute it and/or modify it under
# the terms of the Soopycat License, version 2.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the Soopycat License for more details.

# You should have received a copy of the Soopycat License along with this
# program.  If not, see <https://smatz.net/soopycat>.

import collections.abc

smbox, _ = csm_tutor.question('smallbox')

defaults = dict(smbox['defaults'])

defaults.update({'csq_rows': 10, 'csq_cols': 60,})


def escape(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace(
        '<', '&lt;').replace('>', '&gt;')

total_points = smbox['total_points']
answer_display = smbox['answer_display']
handle_submission = smbox['handle_submission']


def render_html(last_log, **info):
    if last_log is None:
        last_log = {}
    rows = info['csq_rows']
    cols = info['csq_cols']
    out = '<textarea rows="%d" cols="%d"' % (rows, cols)
    out += ' name="%s"' % info['csq_name']
    out += ' id="%s"' % info['csq_name']
    out += '>%s</textarea><br>' % escape(last_log.get(info['csq_name'], ''))
    return out
