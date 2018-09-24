from django.db import models


class Job(models.Model):

    WEST_LAFAYETTE = 'WL'
    LAFAYETTE = 'L'
    CITY_CHOICES = (
        (WEST_LAFAYETTE, 'West Lafayette'),
        (LAFAYETTE, 'Lafayette'),
    )
    title = models.CharField(max_length=380)
    company = models.CharField(max_length=100)
    category = models.CharField(null=True, blank=True, default=None, max_length=380)
    city = models.CharField(
        max_length=2,
        choices=CITY_CHOICES,
        default=LAFAYETTE,
    )
    salary = models.CharField(max_length=100, null=True, blank=True, default=None)
    description = models.TextField()
    instructions = models.TextField()
    logo = models.ImageField(null=True, blank=True, default=None, upload_to='uploads/')
    url = models.URLField(null=True, blank=True, default=None)
    email = models.EmailField(null=True, blank=True, default=None)
    highlight_job = models.BooleanField(null=True, blank=True, default=False)
    # HIGHLIGHT = 'hl'
    # HL_W_LOGO = 'logo'
    # FEATURED = 'fd'
    # LISTING_CHOICES = (
     #   (HIGHLIGHT, 'Yes, highlight my ad'),
      #  (HL_W_LOGO, 'Both, highlight my ad and display my company logo'),
       # (FEATURED, 'Feature my job and pin it to the top'),
    # )
    # listing_type = models.RadioSelect(LISTING_CHOICES)
    featured = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (
            self.title, self.company
        )
    #    return '[%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s]' % (
    #        self.title, self.category, self.city, self.salary, self.description, self.instructions, self.company,
    #        self.url, self.email, self.highlight_job, self.featured, self.published)
