'''

Copyright (c) 2017, Vanessa Sochat, All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''


from shub.settings import ( 
    DOMAIN_NAME,
    DOMAIN_NAKED,
    ENABLE_GOOGLE_AUTH,
    ENABLE_TWITTER_AUTH,
    ENABLE_GITHUB_AUTH,
    ENABLE_GITLAB_AUTH,
    HELP_CONTACT_EMAIL,
    HELP_INSTITUTION_SITE,
    PRIVATE_ONLY,
    REGISTRY_URI,
    REGISTRY_NAME,
    PLUGINS_ENABLED,
)

def domain_processor(request):
    return {'domain': DOMAIN_NAME,
            'DOMAIN_NAKED':DOMAIN_NAKED,
            'REGISTRY_URI': REGISTRY_URI,
            'REGISTRY_NAME':REGISTRY_NAME }


def help_processor(request):
    return {'HELP_CONTACT_EMAIL': HELP_CONTACT_EMAIL,
            'HELP_INSTITUTION_SITE':HELP_INSTITUTION_SITE}

def settings_processor(request):
    return {'PRIVATE_ONLY':PRIVATE_ONLY }


def auth_processor(request):
    return {"ENABLE_GOOGLE_AUTH":ENABLE_GOOGLE_AUTH,
            "ENABLE_TWITTER_AUTH":ENABLE_TWITTER_AUTH,
            "ENABLE_GITHUB_AUTH":ENABLE_GITHUB_AUTH,
            "ENABLE_GITLAB_AUTH":ENABLE_GITLAB_AUTH,
            "PLUGINS_ENABLED":PLUGINS_ENABLED,}


