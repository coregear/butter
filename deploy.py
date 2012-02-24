"""
 Copyright (c) 2012, OMBU Inc. http://ombuweb.com
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:
     * Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.
     * Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.
     * Neither the name of OMBU INC. nor the
       names of its contributors may be used to endorse or promote products
       derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 ARE DISCLAIMED. IN NO EVENT SHALL OMBU INC. BE LIABLE FOR ANY DIRECT,
 INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from __future__ import with_statement
from fabric.api import task, env
from fabric.operations import run

@task
def log():
    """
    Tail a the deployment log of a host
    """
    print('+ Reading deployment log...')
    with cd(env.host_site_path):
        with hide('running', 'stdout'):
            out = run('cat DEPLOYMENTS')
            print(out)

def mark(parsed_ref):
    """
    Mark a deployment
    """
    from time import gmtime, strftime
    print('+ Logging deployment')
    with cd(env.host_site_path):
        with hide('running', 'stdout'):
            if not files.exists('DEPLOYMENTS'):
                print('+ No DEPLOYMENTS file found. Creating one.')
                run('touch DEPLOYMENTS');
            run('chmod u+w DEPLOYMENTS')
            date= strftime("%Y.%m.%d at %H:%M:%SUTC", gmtime())
            run('echo "%s by %s: %s" >> DEPLOYMENTS' % (date, os.getlogin(), parsed_ref))
            run('chmod u-w DEPLOYMENTS')
