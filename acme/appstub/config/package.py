from collections import OrderedDict

# Package configuration is not meant to be overridden when used inside other
# apps.  This information is always unchanged and consistent.  The main
# config/appstub.py however is meant to be overridden per use case.
# This is merged inside the main appstub.py and accessible at
# config('acme.appstub.package')

config = {

    # --------------------------------------------------------------------------
    # Package Information
    # --------------------------------------------------------------------------
    'name': 'acme.appstub',


    # --------------------------------------------------------------------------
    # Package Dependencies (Service Providers)
    #
    # Define all the packages that this package depends on.  At a minimum, only
    # the uvicore.foundation package is required.  The foundation is very
    # minimal and only depends on configuratino, logging and console itself.
    # You must add other core services built into uvicore only if your package
    # requires them.  Services like uvicore.database, uvicore.orm, uvicore.auth
    # uvicore.http, etc...
    # --------------------------------------------------------------------------
    'services': OrderedDict({
        'uvicore.foundation': {
            'provider': 'uvicore.foundation.services.Foundation',
        },
        # 'uvicore.database': {calc
        #     'provider': 'uvicore.database.services.Database',
        # },
        # 'uvicore.orm': {
        #     'provider': 'uvicore.orm.services.Orm',
        # },
        # 'uvicore.auth': {
        #     'provider': 'uvicore.auth.services.Auth',
        # },
        'uvicore.http': {
            'provider': 'uvicore.http.services.Http',
        },
    }),

}
