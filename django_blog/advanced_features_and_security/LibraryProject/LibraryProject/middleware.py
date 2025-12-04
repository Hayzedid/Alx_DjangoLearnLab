"""
Custom middleware for Content Security Policy (CSP) implementation.
This middleware adds CSP headers to protect against XSS attacks.
"""

class CSPMiddleware:
    """
    Middleware to add Content Security Policy headers to all responses.
    This helps prevent XSS attacks by controlling which resources can be loaded.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Set Content Security Policy header
        # This policy allows resources only from the same origin ('self')
        # and inline styles for basic styling needs
        csp_policy = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "font-src 'self'; "
            "connect-src 'self'; "
            "frame-ancestors 'none';"
        )
        
        response['Content-Security-Policy'] = csp_policy
        
        return response
