"""Builds the Challenge Golf static site (Bold Green theme).
Each page shares the same header, footer and swoosh. Run: python3 build.py"""
import os
OUT = os.path.dirname(os.path.abspath(__file__))

NAV = [("index.html", "Home"), ("about.html", "About"), ("programs.html", "Programs"), ("events.html", "Events"),
       ("cg35.html", "CG35 Gala"), ("gallery.html", "Gallery"), ("support.html", "Support Us"),
       ("contact.html", "Contact")]

LOGO = "img/logo.jpg"
EMAIL = "info@challengegolf.ca"
CHARITY = "88986-6570-RR0001"

PHOTOS = {  # caption -> (file in img/photos/, focal point)
    "participants on the range": ("hero-friends", "50% 35%"),
    "volunteers with participants": ("team-friends", "50% 35%"),
    "participant swinging": ("range-powerchair", "50% 55%"),
    "summer program at Tee Zone": ("opening-day", "50% 55%"),
    "winter program indoors": ("winter-stool", "50% 55%"),
    "caregiver group": ("caregiver-chat", "45% 45%"),
    "volunteer helping at the tee": ("coaching-arm", "50% 40%"),
    "Christmas Luncheon": ("christmas-friends", "50% 35%"),
    "GIVEOakville": ("range-smiles", "50% 35%"),
    "CG35 Gala": ("indoor-group", "50% 55%"),
    "Summer BBQ": ("maple-lodge", "50% 45%"),
    "golf tournament at Granite Ridge": ("tournament-adaptive", "50% 50%"),
    "volunteer appreciation": ("boat-help", "50% 40%"),
    "mosaic swing": ("hug", "50% 35%"), "m high five": ("high-five", "50% 45%"), "m bbq": ("bbq-table", "50% 45%"),
    "m winter": ("winter-ramp", "45% 55%"), "m cart": ("cart-friends", "50% 45%"),
    "past tournament": ("putting-brace", "50% 50%"), "past bbq": ("bbq-overview", "50% 50%"),
    "past christmas": ("christmas-room", "45% 50%"), "past cruise": ("boat-group", "50% 50%"),
    "indoor swing": ("winter-team", "50% 50%"), "bbq friends": ("tournament-peace", "50% 45%"), "community social": ("flag-friends", "50% 45%"),
    "Summer Program": ("range-laughs", "50% 50%"), "Golf Tournaments": ("tournament-colour", "50% 45%"),
    "Annual BBQ": ("summer-patio2", "50% 50%"), "Christmas Luncheon album": ("christmas-room", "45% 50%"),
    "Winter Program": ("winter-volunteers", "50% 45%"), "Volunteer Appreciation": ("boat-wave", "50% 50%"),
    "volunteers at Tee Zone": ("winter-coaching", "50% 50%"), "summer patio": ("teezone-patio", "50% 50%"),
    "civitan": ("civitan-cheque", "50% 45%"),
}

def photo(label, i="p", h="100%", sky="#e4f2d0"):
    """Real photo when we have one; otherwise a drawn fairway placeholder with a caption."""
    if label in PHOTOS:
        f, pos = PHOTOS[label]
        return f'<div class="photo" style="height:{h}"><img src="img/photos/{f}.jpg" alt="{label}" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"></div>'
    return f'''<div class="photo" style="height:{h}"><svg viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs><linearGradient id="g{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky}"/><stop offset="1" stop-color="#fbfdf6"/></linearGradient></defs>
<rect width="800" height="500" fill="url(#g{i})"/><circle cx="620" cy="140" r="60" fill="#fff7e0"/>
<path d="M0 320 C180 270 340 300 480 310 S720 270 800 285 V500 H0Z" fill="#8cc63f"/>
<ellipse cx="500" cy="352" rx="160" ry="26" fill="#b9de86" opacity=".8"/>
<line x1="540" y1="282" x2="540" y2="352" stroke="#fff" stroke-width="3"/><path d="M541 282 L578 295 L541 308Z" fill="#b81614"/>
<path d="M0 410 C220 375 430 420 800 395 V500 H0Z" fill="#3c7437"/></svg><span class="tag">Photo needed: {label}</span></div>'''

SWOOSH = '''<div class="swoosh"><svg viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true">
<path d="M0 90 C360 10 760 150 1440 40 V140 H0Z" fill="#8cc63f"/><path d="M0 120 C420 50 820 160 1440 85 V140 H0Z" fill="#f4f7f1"/></svg></div>'''

def header(active):
    links = "".join(
        f'<a href="{h}" class="{"on " if h == active else ""}{"hl" if h == "cg35.html" else ""}">{t}</a>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="wrap nav"><a class="brand" href="index.html"><span class="seal"><img src="{LOGO}" alt="Challenge Golf 35 Years logo"></span>Challenge Golf</a>
<nav class="links" id="menu" aria-label="Main">{links}<a class="btn btn-red" href="support.html#donate">Donate</a></nav>
<button class="burger" aria-label="Open menu" onclick="document.getElementById('menu').classList.toggle('open')">
<svg width="30" height="30" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg></button></div>'''

FOOTER = f'''<footer><div class="wrap"><div class="cols">
<div><div class="fbrand"><span class="seal"><img src="{LOGO}" alt=""></span>Challenge Golf</div>
<p style="margin-top:14px;max-width:320px">Golf for the Physically Challenged. A registered Canadian charity, run entirely by volunteers in Oakville, Ontario since 1992.</p></div>
<div><h5>Explore</h5><a href="index.html">Home</a><a href="about.html">About Us</a><a href="programs.html">Programs</a><a href="events.html">Events</a><a href="gallery.html">Gallery</a></div>
<div><h5>Get involved</h5><a href="support.html#donate">Donate</a><a href="support.html#volunteer">Volunteer</a><a href="support.html#sponsor">Sponsor</a><a href="cg35.html">CG35 Gala</a></div>
<div><h5>Contact</h5><a href="mailto:{EMAIL}">{EMAIL}</a><a>Facebook</a><a>Instagram @challengegolf1992</a><a>LinkedIn</a></div>
</div><div class="legal"><span>© 2026 Challenge Golf · Golf for the Physically Challenged</span><span>Charity registration number {CHARITY}</span></div></div></footer>'''

VIDEO_JS = r"""<script>
document.querySelectorAll('.video[data-yt]').forEach(function(v){v.addEventListener('click',function(e){
 e.preventDefault();var f=document.createElement('iframe');
 f.src='https://www.youtube-nocookie.com/embed/'+v.dataset.yt+'?autoplay=1&rel=0';
 f.title=v.getAttribute('aria-label');f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;
 v.classList.add('playing');v.replaceChildren(f);});});
</script>"""

def page(fname, title, desc, hero, main):
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="icon" href="{LOGO}"><link rel="stylesheet" href="css/style.css"></head>
<body><div class="top">{header(fname)}{hero}</div>{SWOOSH}<main id="main">{main}</main>{FOOTER}{VIDEO_JS}</body></html>'''
    open(os.path.join(OUT, fname), "w").write(html)

HERO_IMG = {"About us": ("group-lanai", "50% 50%"), "Programs": ("swing-follow", "50% 40%"), "Events": ("group-teezone", "50% 50%"),
            "Gallery": ("flag-friends", "50% 45%"), "Support us": ("volunteers-gazebo", "50% 50%"), "Contact": ("patio-friends", "50% 45%")}

def phero(kicker, title, text):
    f, pos = HERO_IMG[kicker]
    return (f'<div class="wrap phero has-img"><div><span class="kicker">{kicker}</span><h1>{title}</h1><p>{text}</p></div>'
            f'<div class="phimg"><img src="img/photos/{f}.jpg" alt="" style="object-position:{pos}"></div></div>')

def banner_cg35(green=False):
    return f'''<div class="banner{' green' if green else ''}"><span class="seal"><img src="{LOGO}" alt=""></span>
<div><h3>35th Anniversary Celebration</h3><p>Saturday, April 17, 2027 · 2–9 pm · Oakville Conference Centre</p></div>
<a class="btn" href="https://ocf.fcsuite.com/erp/donate/list/event?event_date_id=2274" target="_blank" rel="noopener">Get tickets</a></div>'''

# ------------------------------------------------------------------ HOME
page("index.html", "Challenge Golf | Golf for the Physically Challenged, Oakville",
     "Free, volunteer-led golf for adults with physical challenges in Oakville since 1992.",
     f'''<div class="wrap hero"><div><span class="kicker">35 years · Oakville · Registered Canadian charity</span>
<h1>Believe<br>and <b>achieve.</b></h1>
<p>Challenge Golf helps people living with neurological, physical and developmental limitations enjoy a more active, fulfilling life through golf. Free weekly programs, run entirely by volunteers since 1992.</p>
<div class="btns"><a class="btn btn-red" href="programs.html">Join a program</a><a class="btn btn-ghost" href="support.html">Support us</a></div></div>
<div class="ring"><div class="ph"><img src="img/photos/group-teezone.jpg" alt="Challenge Golf members waving at Tee Zone"></div><div class="s"><img src="{LOGO}" alt="Challenge Golf 35 Years: Believe and Achieve"></div></div></div>''',
     f'''<div class="wrap"><div class="stats"><div><b>Since 1992</b><span>adaptive golf in Oakville</span></div><div><b>100%</b><span>volunteer-run</span></div>
<div><b>No fees</b><span>for participants</span></div><div><b>Year-round</b><span>summer range & winter indoor</span></div></div></div>

<section><div class="wrap split"><div><span class="sec-k">Our mission</span><h2>More than a game</h2>
<div class="prose"><p>Our mission is to empower community members facing physical limitations, aiding them in their journey towards a more active and fulfilling life, both physically and mentally.</p>
<p>We expand opportunities for fellowship by providing a dedicated space, equipment and guidance. Our volunteers offer advice, tuition and encouragement so every participant can play the game to the fullest extent of their abilities.</p></div>
<div class="btns" style="margin-top:24px"><a class="btn btn-green" href="about.html">Our story</a></div></div>
<a class="video" href="https://www.youtube.com/watch?v=BDqtwIrgS60" data-yt="BDqtwIrgS60" aria-label="Play video: Golf for Everyone"><img src="img/photos/hero-friends.jpg" alt="Two Challenge Golf members smiling"><span class="play" aria-hidden="true">▶</span><span class="cap">Watch: Golf for Everyone (1 min)</span></a></div></section>

<section class="white"><div class="wrap"><span class="sec-k">Programs</span><h2>Find your program</h2>
<div class="grid3">
<div class="card"><h3>Summer Program</h3><p>Weekly sessions on the driving range at Tee Zone, May to early October.</p><div class="m">Mondays · 1:00–2:30 pm</div><a class="more" href="programs.html#summer">Details →</a></div>
<div class="card g"><h3>Winter Program</h3><p>Keep your swing going all winter on indoor simulators at Birdies Indoor Golf.</p><div class="m">Mondays · 1–3 pm · from Jan 11, 2027</div><a class="more" href="programs.html#winter">Details →</a></div>
<div class="card r"><h3>Caregiver Support</h3><p>"Beyond Caregiving": a monthly support group for the people who make participation possible.</p><div class="m">Monthly · St. Paul's United Church</div><a class="more" href="programs.html#caregivers">Details →</a></div>
</div></div></section>

<section><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:16px"><div><span class="sec-k">Events</span><h2 style="margin-bottom:0">Coming up</h2></div><a class="more" style="color:var(--red);font-weight:700" href="events.html">All events →</a></div>
<div class="ev" style="margin-top:26px">
<a href="events.html"><small>NOV 13 – DEC 7</small><h4>GIVEOakville 2026</h4><p>Support us in the Oakville Community Foundation's giving campaign.</p></a>
<a href="events.html#christmas"><small>MON · NOV 30</small><h4>Christmas Luncheon</h4><p>Noon at Mandarin Erin Mills · $25</p></a>
<a href="programs.html#winter"><small>MON · JAN 11</small><h4>Winter Program begins</h4><p>Mondays 1–3 pm at Birdies Indoor Golf</p></a>
</div><div style="margin-top:40px">{banner_cg35()}</div></div></section>

<section style="padding-top:0"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:16px"><div><span class="sec-k">Life at Challenge Golf</span><h2 style="margin-bottom:0">Believe. Swing. Belong.</h2></div><a style="color:var(--red);font-weight:700" href="gallery.html">See the gallery →</a></div>
<div class="mosaic"><div class="m1">{photo("mosaic swing","hm1")}</div><div class="m2">{photo("m high five","hm2")}</div><div class="m3">{photo("m bbq","hm3")}</div><div class="m4">{photo("m winter","hm4")}</div><div class="m5">{photo("m cart","hm5")}</div></div></div></section>

''')

# ------------------------------------------------------------------ ABOUT
board = ["Andy Liu", "Danny Foran", "Jason Vale", "Anne Lamont", "Andy Westcott", "Tamara Boaden",
         "Susan Barber Kahro", "Darryl Clarence", "Neil Huddlestone", "Sharon Brodner"]
page("about.html", "About Us | Challenge Golf", "Our mission, history and board of directors.",
     phero("About us", "Our story", "Golf for the Physically Challenged, also known as Challenge Golf, is a registered Canadian charity based in Oakville, Ontario."),
     f'''<section><div class="wrap split"><div class="rounded" style="height:440px">{photo("volunteers with participants", "a1")}</div>
<div><span class="sec-k">Our mission</span><h2>Empowering active, fulfilling lives</h2><div class="prose">
<p>Our mission is to empower community members facing physical limitations, aiding them in their journey towards a more active and fulfilling life, both physically and mentally.</p>
<p>We strive to expand opportunities for fellowship by providing a dedicated space, necessary equipment, and guidance.</p>
<p>Our team of volunteers is committed to offering advice, tuition, and encouragement, enabling participants to learn and play the game of golf to the fullest extent of their abilities.</p></div></div></div></section>

<section class="white"><div class="wrap split top-align"><div><span class="sec-k">History</span><h2>Our journey</h2>
<p class="lead">From a driving range in 1990 to a year-round program today. We're grateful to everyone who has contributed along the way. Together, let's keep making our community an even better place.</p></div>
<div class="timeline">
<div><b>1990</b><p><strong>Where it all began.</strong> Challenge Golf starts out at the Family Golf Driving Range in Oakville.</p></div>
<div><b>1992</b><p><strong>A registered charity.</strong> Golf for the Physically Challenged becomes an officially registered Canadian charity.</p></div>
<div><b>2013</b><p><strong>A new home at Tee Zone.</strong> We move to Tee Zone Driving Range, owned by BOT Construction, which has generously let us use its range free of charge ever since.</p></div>
<div><b>2023</b><p><strong>Tournament days.</strong> We launch two annual tournaments at Granite Ridge Golf Club.</p></div>
<div><b>2024</b><p><strong>Golf all year round.</strong> Our winter indoor program begins at Birdies Indoor Golf in Oakville, making Challenge Golf a year-round program.</p></div>
<div><b>2024</b><p><strong>A holiday tradition.</strong> We hold our first Christmas gathering, bringing members together for the holiday season.</p></div>
<div><b>Today</b><p><strong>Still growing.</strong> Weekly summer and winter programs, tournaments, social events and new caregiver support, all run by volunteers. In 2027 we celebrate 35 years. <a href="cg35.html" style="color:var(--red);font-weight:700">Join the celebration →</a></p></div>
</div></div></section>

<section id="participants"><div class="wrap split"><div><span class="sec-k">Who we serve</span><h2>Our participants</h2><div class="prose">
<p>Our participants are valued members of the local community living with neurological, physical and developmental limitations. We cater to their varied and specific needs and provide a supportive environment for their golfing journey.</p>
<p>No previous golf experience or fees are required. Many participants come from Oakville, and we warmly welcome people from across the Greater Toronto Area.</p>
<p>Visitors curious about the program are always welcome to drop by a session.</p></div>
<div class="btns" style="margin-top:22px"><a class="btn btn-red" href="contact.html">Ask about joining</a></div></div>
<div class="rounded" style="height:420px">{photo("participant swinging", "a2", sky="#e2f0f4")}</div></div></section>

<section class="white"><div class="wrap"><span class="sec-k">Leadership</span><h2>Board of directors</h2>
<div class="board">{''.join(f"<div>{n}</div>" for n in board)}<div>Grant Fraser<small>Industry Advisor</small></div></div>
<p style="margin-top:18px"><span class="note">Add roles (Chair, Treasurer, Secretary…) and headshots if you like</span></p></div></section>''')

# ------------------------------------------------------------------ PROGRAMS
def pcard(id_, title, chip, text, facts, label, sky):
    f = "".join(f"<div><em>{k}</em><span>{v}</span></div>" for k, v in facts)
    return f'''<div class="pcard" id="{id_}">{photo(label, id_, sky=sky)}<div class="body"><span class="chip">{chip}</span>
<h3 style="margin-top:12px">{title}</h3><p style="color:var(--muted);margin-top:8px">{text}</p><div class="facts">{f}</div>
<div class="btns"><a class="btn btn-red" href="contact.html">Register interest</a></div></div></div>'''

page("programs.html", "Programs | Challenge Golf", "Summer, winter and caregiver support programs.",
     phero("Programs", "Play all year", "There are no fees to participate. Donations are gratefully accepted when they're within a participant's means."),
     f'''<section><div class="wrap">
{pcard("summer","Summer Program","May – early October","Weekly sessions on the driving range and golf course, tailored for people with physical limitations. Volunteers and our golf cart help participants get from the parking lot to our reserved tees.",
 [("When","Mondays, 1:00–2:30 pm (except statutory holidays)"),("Season","Early May to the start of October"),("Where","Tee Zone Driving Range, 4105 Bronte Rd (north of Hwy 407), Oakville"),("Cost","Free")],"summer program at Tee Zone","#e4f2d0")}
{pcard("winter","Winter Program","January – spring","Keep your swing going through the winter on indoor golf simulators, in a warm, relaxed setting with the same friendly volunteers.",
 [("When","Mondays, 1–3 pm"),("Starts","January 11, 2027"),("Where","Birdies Indoor Golf, Oakville"),("Cost","Free")],"winter program indoors","#e2f0f4")}
{pcard("caregivers","Beyond Caregiving","New in 2026","A support group for caregivers. Several participants told us their caregivers were struggling, and that affects whether they can take part. This group gives caregivers time, support and community of their own.",
 [("When","One 2-hour session a month, Thursdays"),("Where","St. Paul's United Church, Oakville"),("Led by","A professional facilitator"),("Cost","Free")],"caregiver group","#fde9e4")}
<div class="banner green" style="margin-top:40px"><span class="seal"><img src="{LOGO}" alt=""></span><div><h3>Registration</h3><p>Spaces are limited. Registration forms go to participants each season, so contact us to be added to the list.</p></div><a class="btn" href="contact.html">Contact us</a></div>
</div></section>

<section class="white"><div class="wrap split"><div><span class="sec-k">What to expect</span><h2>Your first session</h2>
<ul class="ticks"><li>No golf experience is needed. Volunteers offer advice, tuition and encouragement.</li><li>Clubs and balls are provided, and tees are kept full by volunteers.</li><li>Our golf cart can take you from the parking lot to the reserved tees.</li><li>Participants arrange their own transportation to the site.</li><li>Participants should be able to manage their basic needs independently or with a little help.</li></ul></div>
<div class="rounded" style="height:380px">{photo("volunteer helping at the tee", "x1")}</div></div></section>''')

# ------------------------------------------------------------------ EVENTS
def erow(id_, mon, day, sub, title, text, chip, label, sky="#e4f2d0"):
    return f'''<div class="erow" id="{id_}"><div class="date"><small>{mon}</small><b>{day}</b><span>{sub}</span></div>
<div><span class="chip{' red' if 'TBA' in chip or 'Save' in chip else ''}">{chip}</span><h3 style="margin-top:8px">{title}</h3><p>{text}</p></div>{photo(label, id_, h="170px", sky=sky)}</div>'''

page("events.html", "Events | Challenge Golf", "Tournaments, BBQ, Christmas Luncheon and more.",
     phero("Events", "Golf, food & friendship", "Our events bring participants, families, volunteers and supporters together all year round."),
     f'''<section><div class="wrap">
{erow("christmas","NOV","30","Monday","Christmas Luncheon","Noon at Mandarin Erin Mills, $25 per person. Our festive gathering for participants, families and volunteers, with a short talk on staying well through the holiday season.","Upcoming","Christmas Luncheon","#fde9e4")}
{erow("give","NOV","13","to Dec 7","GIVEOakville 2026","We're taking part in the Oakville Community Foundation's giving campaign. Every gift helps keep our programs free.","Fundraising","GIVEOakville","#eef6dc")}
{erow("cg35","APR","17","2027","35th Anniversary Celebration","2–9 pm at the Oakville Conference Centre. Join us to celebrate 35 years of Challenge Golf.","Save the date","CG35 Gala","#fde9e4")}
{erow("bbq","JUL","TBA","2027","Annual Summer BBQ","Held at Tee Zone Driving Range. The 2026 BBQ was sponsored by Maple Lodge Farms for the third year in a row. Stay tuned for the 2027 date.","Date TBA","Summer BBQ")}
{erow("tournaments","AUG","TBA","2027","Golf Tournaments","Hosted by Granite Ridge Golf Club for four consecutive years. In 2026 we played Monday, August 24 and Monday, October 19, with a 10:00 am tee-off.","Dates TBA","golf tournament at Granite Ridge","#e2f0f4")}
{erow("volunteers","TBA","★","","Volunteer Appreciation","A thank-you celebration for the volunteers who make every session possible.","Date TBA","volunteer appreciation","#eef6dc")}
</div></section>
<section class="white"><div class="wrap center"><h2>Photos from past events</h2><p class="lead">Tournaments, BBQs and luncheons through the years.</p><div class="grid4">{photo("past tournament","pe1",h="200px")}{photo("past bbq","pe2",h="200px")}{photo("past christmas","pe3",h="200px")}{photo("past cruise","pe4",h="200px")}</div><a class="btn btn-green" style="margin-top:22px" href="gallery.html">Visit the gallery</a></div></section>''')

# ------------------------------------------------------------------ CG35
page("cg35.html", "CG35 Gala | Challenge Golf 35th Anniversary", "Celebrate 35 years of Challenge Golf on April 17, 2027.",
     f'''<div class="wrap cg-hero"><span class="seal"><img src="{LOGO}" alt="Challenge Golf 35 Years: Believe and Achieve"></span>
<div><span class="kicker">CG35 · 1992–2027</span><h1 style="font-family:var(--serif);font-size:64px;font-weight:400;text-transform:uppercase;line-height:1.02;margin-top:12px">35th Anniversary<br>Celebration</h1>
<p style="font-size:20px;opacity:.9;margin:16px 0 28px">Saturday, April 17, 2027 · 2–9 pm · Oakville Conference Centre</p>
<div class="btns"><a class="btn btn-red" href="https://ocf.fcsuite.com/erp/donate/list/event?event_date_id=2274" target="_blank" rel="noopener">Get tickets</a><a class="btn btn-ghost" href="#sponsor">Become a sponsor</a></div></div></div>''',
     f'''<section><div class="wrap split top-align"><div><span class="sec-k">The celebration</span><h2>Thirty-five years of believing and achieving</h2><div class="prose">
<p>Since 1992, Challenge Golf has helped people living with physical challenges enjoy the game. On April 17, 2027 we're celebrating with the participants, families, volunteers and supporters who made it happen.</p>
<p>Join us for an afternoon and evening of stories, celebration and community, and help us raise funds for the next 35 years.</p></div>
<p style="margin-top:14px"><span class="note">Add the program: dinner, speakers, activities, auction…</span></p></div>
<div class="ticket" id="tickets"><h3 style="font-family:var(--serif);font-size:28px;font-weight:400;text-transform:uppercase;margin-bottom:10px">Event details</h3>
<div class="row"><span>Date</span><b>Saturday, April 17, 2027</b></div><div class="row"><span>Time</span><b>2:00 – 9:00 pm</b></div>
<div class="row"><span>Venue</span><b>Oakville Conference Centre</b></div><div class="row"><span>Tickets</span><b>On sale now</b></div>
<a class="btn btn-red" href="https://ocf.fcsuite.com/erp/donate/list/event?event_date_id=2274" target="_blank" rel="noopener" style="display:block;text-align:center;margin-top:18px">Buy tickets</a></div></div></section>

<section class="white" id="sponsor"><div class="wrap"><span class="sec-k">Sponsorship</span><h2>Sponsor CG35</h2><p class="lead">Put your organization in front of our community and help keep adaptive golf free for everyone.</p>
<div class="tiers" style="margin-top:30px">
<div class="tier"><b>Friend</b><p>Benefits package coming soon</p></div><div class="tier"><b>Silver</b><p>Benefits package coming soon</p></div><div class="tier"><b>Gold</b><p>Benefits package coming soon</p></div><div class="tier"><b>Presenting</b><p>Benefits package coming soon</p></div></div>
<div class="btns" style="margin-top:28px"><a class="btn btn-red" href="contact.html">Enquire about sponsorship</a></div></div></section>

<section><div class="wrap"><span class="sec-k">35 years in pictures</span><h2>Our community today</h2>
<div class="grid3">{photo("indoor swing","c1",h="280px")}{photo("bbq friends","c2",h="280px")}{photo("community social","c3",h="280px")}</div></div></section>''')

# ------------------------------------------------------------------ GALLERY
albums = [("Summer Program", "Mondays at Tee Zone", "#e4f2d0"), ("Golf Tournaments", "Granite Ridge, 2023–2025", "#e2f0f4"),
          ("Annual BBQ", "Thanks to Maple Lodge Farms", "#fde9e4"), ("Christmas Luncheon album", "Festive gatherings", "#fde9e4"),
          ("Winter Program", "Indoor simulators", "#e2f0f4"), ("Volunteer Appreciation", "Thank-you cruise, 2026", "#eef6dc")]
page("gallery.html", "Gallery | Challenge Golf", "Photos and videos from Challenge Golf programs and events.",
     phero("Gallery", "Moments on the course", "Photos and videos from our programs, tournaments and celebrations."),
     f'''<section><div class="wrap"><div class="grid2"><a class="video" href="https://www.youtube.com/watch?v=BDqtwIrgS60" data-yt="BDqtwIrgS60" aria-label="Play video: Challenge Golf: our story"><img src="img/photos/winter-lounge.jpg" alt="Members together at Birdies Indoor Golf"><span class="play" aria-hidden="true">▶</span><span class="cap">Challenge Golf: our story</span></a>
<a class="video" href="https://www.youtube.com/watch?v=tVcAj_22jJY" data-yt="tVcAj_22jJY" aria-label="Play video: Summer Program highlights"><img src="img/photos/summer-patio2.jpg" alt="Members on the Tee Zone patio"><span class="play" aria-hidden="true">▶</span><span class="cap">Summer Program highlights</span></a></div></div></section>
<section style="padding-top:0"><div class="wrap"><h2>Albums</h2><div class="albums">
{''.join(f'<div class="album">{photo(t, "al"+str(i), sky=s)}<div class="b"><h3>{t.replace(" album","")}</h3><span>{d}</span></div></div>' for i,(t,d,s) in enumerate(albums))}
</div></div></section>''')

# ------------------------------------------------------------------ SUPPORT US
sponsors = [("tee-zone", "Tee Zone Driving Range"), ("granite-ridge", "Granite Ridge Golf Club"), ("civitan-oakville", "Civitan Club of Oakville"),
            ("paragolf-ontario", "Paragolf Ontario"), ("golf-journalists", "Golf Journalists Association of Canada"),
            ("golf-canada-foundation", "Golf Canada Foundation"), ("enbridge", "Enbridge Fueling Futures"),
            ("mind-forward", "Mind Forward Brain Injury Services"), ("passion-for-parkinsons", "Passion for Parkinson's Foundation"),
            ("oakville-strokers", "Oakville Strokers")]
icon = lambda p: f'<span class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#25502a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg></span>'
page("support.html", "Support Us | Challenge Golf", "Donate, volunteer, sponsor or donate golf equipment.",
     phero("Support us", "Help every golfer swing", "Challenge Golf is run entirely by volunteers, so every donation goes directly to our programs."),
     f'''<section><div class="wrap"><div class="help">
<a href="#donate">{icon('<path d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z"/>')}<h3>Donate</h3><p>Instant tax receipts for every gift.</p></a>
<a href="#volunteer">{icon('<circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2M16 3.1a4 4 0 0 1 0 7.8M21 21v-2a4 4 0 0 0-3-3.9"/>')}<h3>Volunteer</h3><p>Join us at the range on Mondays.</p></a>
<a href="#sponsor">{icon('<path d="M12 2l3 6.5 7 .8-5.2 4.8 1.4 7L12 17.8 5.8 21.1l1.4-7L2 9.3l7-.8z"/>')}<h3>Sponsor</h3><p>Partner with us on events and CG35.</p></a>
<a href="#equipment">{icon('<path d="M8 3v14"/><path d="M8 3l8 3-8 3"/><circle cx="15" cy="19" r="2.5"/>')}<h3>Donate equipment</h3><p>Clubs, balls, bags and accessories.</p></a>
</div></div></section>

<section class="white" id="donate"><div class="wrap split top-align"><div><span class="sec-k">Donate</span><h2>Why donate?</h2>
<p class="lead">Your generosity fuels the growth of Challenge Golf and ensures people of all abilities continue to experience the joy and empowerment that golf brings.</p>
<div class="why" style="grid-template-columns:1fr"><div><b>Empower lives</b><span>Your donation directly supports programs that empower people of all abilities through golf.</span></div>
<div><b>Foster inclusivity</b><span>Everyone, regardless of ability, belongs on the driving range and golf course.</span></div>
<div><b>Make a lasting impact</b><span>Your gift helps us reach more people and introduce new programs.</span></div></div></div>
<div class="ticket"><h3 style="font-family:var(--serif);font-size:28px;font-weight:400;text-transform:uppercase">Make a donation</h3>
<p style="color:var(--muted);margin:8px 0 18px">Challenge Golf is a registered Canadian charity ({CHARITY}). Immediate tax receipts are available.</p>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px">{''.join(f'<span style="border:2px solid {"#25502a;background:#25502a;color:#fff" if a=="$100" else "#e2e9dc"};border-radius:10px;text-align:center;padding:12px 0;font-weight:700">{a}</span>' for a in ["$25","$50","$100","Other"])}</div>
<a class="btn btn-red" style="display:block;text-align:center">Donate securely</a><p style="font-size:13.5px;color:var(--muted);margin-top:12px;text-align:center">Opens our secure donation page</p></div></div></section>

<section id="volunteer"><div class="wrap split"><div class="rounded" style="height:420px">{photo("volunteers at Tee Zone", "v1")}</div>
<div><span class="sec-k">Volunteer</span><h2>Be part of the team</h2><p class="lead">Volunteers create a friendly, safe environment. Chatting with participants and helping with equipment is at the heart of it.</p>
<ul class="ticks"><li>Set up the Challenge Golf section and semi-automated tees at Tee Zone</li><li>Keep tees stocked with golf balls and hand out clubs</li><li>Bring water to participants</li><li>Drive participants from the parking lot to our tees by golf cart</li></ul>
<div class="btns"><a class="btn btn-red" href="contact.html">I'd like to volunteer</a></div>
<p style="color:var(--muted);font-size:15px;margin-top:12px">Or drop by and say hello at a Monday session.</p></div></div></section>

<section class="white" id="equipment"><div class="wrap split"><div><span class="sec-k">Equipment</span><h2>Donate your golf clubs</h2>
<p class="lead">We welcome new or gently used golf clubs, balls, bags, grips and other accessories. At the moment we can only accept donations in and around the Halton and Peel regions.</p>
<div class="btns" style="margin-top:24px"><a class="btn btn-green" href="contact.html">Arrange a drop-off</a></div></div>
<div id="sponsor" class="card r" style="padding:36px"><span class="sec-k">Sponsor</span><h3 style="font-family:var(--serif);font-size:30px;font-weight:400;text-transform:uppercase;margin-top:6px">Partner with us</h3>
<p>Support our tournaments, BBQ, Christmas Luncheon or the CG35 celebration, and be recognized on our website and at events.</p><a class="btn btn-red" href="contact.html">Sponsorship enquiries</a></div></div></section>

<section id="supporters"><div class="wrap center"><span class="sec-k">Thank you</span><h2>Our supporters</h2><p class="lead">Our recent supporters have included:</p><div class="thanks">{photo("civitan","cv1",h="320px")}<p>Thank you to the Civitan Club of Oakville and every organization that helps keep Challenge Golf free for participants.</p></div>
<div class="logos" style="margin-top:30px">{''.join(f'<div><img src="img/sponsors/{s}.png" alt="{n}"></div>' for s,n in sponsors)}<div class="txt">Maple Lodge Farms</div><div class="txt">Oakville Community Foundation</div></div></div></section>''')

# ------------------------------------------------------------------ CONTACT
page("contact.html", "Contact Us | Challenge Golf", "Get in touch with Challenge Golf.",
     phero("Contact", "We'd love to hear from you", "Questions about programs, volunteering, sponsorship or donations? Send us a message."),
     f'''<section><div class="wrap split top-align"><div>
<div class="info"><div><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div><small>Summer program location</small>Tee Zone Driving Range<br>4105 Bronte Road (north of Hwy 407), Oakville, ON</div>
<div><small>Winter program location</small>Birdies Indoor Golf, Oakville</div>
<div><small>Follow us</small>Facebook · Instagram @challengegolf1992 · LinkedIn</div></div>
<div class="map" style="margin-top:26px">{photo("summer patio","m1")}<a class="btn btn-red maplink" href="https://maps.google.com/?q=Tee+Zone+Driving+Range+4105+Bronte+Road+Oakville">Get directions to Tee Zone</a></div></div>
<div class="ticket"><h3 style="font-family:var(--serif);font-size:28px;font-weight:400;text-transform:uppercase;margin-bottom:16px">Send a message</h3>
<form><div class="f2"><div class="f">Your name</div><div class="f">Email</div></div><div class="f">Phone (optional)</div>
<div class="f">I'm interested in… Joining a program · Volunteering · Sponsoring · Donating · Other</div>
<div class="f tall">Message</div><a class="btn btn-red" style="justify-self:start">Send message</a></form></div></div></section>''')

print("built", [f for f in os.listdir(OUT) if f.endswith(".html")])
