import webapp2, os, json
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch

class MainPage(webapp2.RequestHandler):
    def get(self):
        url = 'https://www.parse.com/jobs/apply'
        data = {'name': 'Dan Salmonsen',
                'email': 'dan@salmonsen.org',
                'position': 'Inside Sales Representative',
                'about': 'I like making technology easier for people to understand and am looking to transition into a sales role that can leverage my experience.  Excellent at communicating with technical and non-technical customers.  Experienced in a wide range of marketing and sales functions in startups to $0.5B prep-IPO and public companies',
                'urls': ['http://parse-proxy.appspot.com', 'https://github.com/dansalmo/parse-proxy']
                }
        headers = {'Content-type': 'application/json'}
        result = urlfetch.fetch(url = url,
                                payload = json.dumps(data),
                                method = urlfetch.POST,
                                headers = headers
                                )
        template_values = {
            'result': result.status_code
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html' )
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', MainPage)],
                      debug=True)
