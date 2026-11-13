"""Builds the Challenge Golf static site (Bold Green theme).
Each page shares the same header, footer and swoosh. Run: python3 build.py"""
import os
OUT = os.path.dirname(os.path.abspath(__file__))
import time
VERSION = time.strftime("%Y%m%d%H%M")  # changes every build so browsers load the newest styles

NAV = [("index.html", "Home"), ("about.html", "About"), ("programs.html", "Programs"), ("events.html", "Schedule & Events"),
       ("cg35.html", "CG35 Gala"), ("gallery.html", "Gallery"), ("support.html", "Support Us"),
       ("contact.html", "Contact")]

LOGO = "img/logo.jpg"
EMAIL = "info@challengegolf.ca"
CHARITY = "88986-6570-RR0001"
FB = "https://www.facebook.com/profile.php?id=61550304226608"
LI = "https://www.linkedin.com/company/challengegolf"
IG = "https://www.instagram.com/challengegolf1992"
SOCIAL = f'<a href="{FB}" target="_blank" rel="noopener">Facebook @challengegolf</a><a href="{LI}" target="_blank" rel="noopener">LinkedIn @challengegolf</a><a href="{IG}" target="_blank" rel="noopener">Instagram @challengegolf1992</a>'
BIRDIES = "Birdies Indoor Golf Oakville<br>504 Iroquois Shore Rd, Unit 8, Oakville, ON L6H 3K4"
BIRDIES_MAP = "https://maps.google.com/?q=Birdies+Indoor+Golf+504+Iroquois+Shore+Rd+Unit+8+Oakville+ON+L6H+3K4"

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
<svg width="30" height="30" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" stroke="#1d3d21" stroke-width="2" stroke-linecap="round"/></svg></button></div>'''

FOOTER = f'''<footer><div class="wrap"><div class="cols">
<div><div class="fbrand"><span class="seal"><img src="{LOGO}" alt=""></span>Challenge Golf</div>
<p style="margin-top:14px;max-width:320px">Golf for the Physically Challenged. A registered Canadian charity, run entirely by volunteers in Oakville, Ontario since 1992.</p></div>
<div><h5>Explore</h5><a href="index.html">Home</a><a href="about.html">About Us</a><a href="programs.html">Programs</a><a href="events.html">Schedule &amp; Events</a><a href="gallery.html">Gallery</a></div>
<div><h5>Get involved</h5><a href="support.html#donate">Donate</a><a href="support.html#volunteer">Volunteer</a><a href="support.html#sponsor">Sponsor</a><a href="cg35.html">CG35 Gala</a></div>
<div><h5>Contact</h5><a href="mailto:{EMAIL}">{EMAIL}</a>{SOCIAL}</div>
</div><div class="legal"><span>© 2026 Challenge Golf · Golf for the Physically Challenged</span><span>Charity registration number {CHARITY}</span></div></div></footer>'''

VIDEO_JS = r"""<script>
(function(){var h=document.getElementById('sitehead');function f(){h.classList.toggle('scrolled',window.scrollY>40)}window.addEventListener('scroll',f,{passive:true});f();})();
document.querySelectorAll('.video[data-yt]').forEach(function(v){v.addEventListener('click',function(e){
 e.preventDefault();var f=document.createElement('iframe');
 f.src='https://www.youtube-nocookie.com/embed/'+v.dataset.yt+'?autoplay=1&rel=0';
 f.title=v.getAttribute('aria-label');f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;
 v.classList.add('playing');v.replaceChildren(f);});});
</script>"""

def page(fname, title, desc, hero, main, extra_head=""):
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{extra_head}
<title>{title}</title><meta name="description" content="{desc}"><link rel="icon" href="{LOGO}"><link rel="stylesheet" href="css/style.css?v={VERSION}"></head>
<body><header class="sitehead" id="sitehead">{header(fname)}</header><div class="top">{hero}</div>{SWOOSH}<main id="main">{main}</main>{FOOTER}{VIDEO_JS}</body></html>'''
    open(os.path.join(OUT, fname), "w").write(html)

HERO_IMG = {"Members": ("winter-team", "50% 50%"), "About us": ("group-lanai", "50% 50%"), "Programs": ("range-lineup", "50% 60%"), "Events": ("putting-green-four", "50% 45%"),
            "Gallery": ("tournament-five", "50% 45%"), "Support us": ("simulator-lesson", "50% 45%"), "Contact": ("course-cart", "50% 60%")}

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
     f'''<div class="wrap"><div class="stats"><div><b>Since 1992</b><span>registered Canadian charity</span></div><div><b>100%</b><span>volunteer-run</span></div>
<div><b>Free program</b><span>for participants</span></div><div><b>Year-round</b><span>summer range & winter indoor</span></div><div><b>More than golf</b><span>building a supportive and encouraging community</span></div></div></div>

<section id="mission"><div class="wrap split"><div><span class="sec-k">Our mission</span><h2>More than a game</h2>
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

<section><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:16px"><div><span class="sec-k">Events</span><h2 style="margin-bottom:0">Coming up</h2></div><a class="more" style="color:var(--red);font-weight:700" href="events.html">Full schedule →</a></div>
<div class="ev" style="margin-top:26px">
<a href="events.html"><small>NOV 13 – DEC 7</small><h4>GIVEOakville 2026</h4><p>Support us in the Oakville Community Foundation's giving campaign.</p></a>
<a href="events.html#christmas"><small>MON · NOV 30</small><h4>Christmas Luncheon</h4><p>Noon at Mandarin Erin Mills · $25 cash only</p></a>
<a href="programs.html#winter"><small>MON · JAN 11</small><h4>Winter Program begins</h4><p>Mondays 1–3 pm at Birdies Indoor Golf</p></a>
</div><div style="margin-top:40px">{banner_cg35()}</div></div></section>

<section style="padding-top:0"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:16px"><div><span class="sec-k">Life at Challenge Golf</span><h2 style="margin-bottom:0">Believe. Swing. Belong.</h2></div><a style="color:var(--red);font-weight:700" href="gallery.html">See the gallery →</a></div>
<div class="mosaic"><div class="m1">{photo("mosaic swing","hm1")}</div><div class="m2">{photo("m high five","hm2")}</div><div class="m3">{photo("m bbq","hm3")}</div><div class="m4">{photo("m winter","hm4")}</div><div class="m5">{photo("m cart","hm5")}</div></div></div></section>

''')

# ------------------------------------------------------------------ ABOUT
board = ["Andy Liu", "Danny Foran", "Jason Vale", "Anne Lamont", "Andy Westcott",
         "Susan Barber Kahro", "Darryl Clarence", "Neil Huddlestone", "Sharon Brodner"]
page("about.html", "About Us | Challenge Golf", "Our mission, history and board of directors.",
     phero("About us", "Our story", "Golf for the Physically Challenged, also known as Challenge Golf, is a registered Canadian charity based in Oakville, Ontario."),
     f'''<section><div class="wrap split"><div class="rounded" style="height:440px">{photo("volunteers with participants", "a1")}</div>
<div><span class="sec-k">Who we are</span><h2>A community built around golf</h2><div class="prose">
<p>For more than three decades, Challenge Golf has brought people living with neurological, physical and developmental limitations together with volunteers who love the game.</p>
<p>We are 100% volunteer-run, and our programs are free for participants. Week after week, what keeps people coming back is the friendship, encouragement and sense of belonging as much as the golf.</p></div>
<div class="btns" style="margin-top:22px"><a class="btn btn-green" href="index.html#mission">Read our mission</a></div></div></div></section>

<section class="white"><div class="wrap"><div class="center" style="max-width:720px;margin:0 auto"><span class="sec-k">History</span><h2>Our journey</h2><p class="lead">From a driving range in 1990 to a year-round program today. We're grateful to everyone who has contributed along the way. Together, let's keep making our community an even better place.</p></div><div class="zz"><div class="zi l"><div class="zc"><b>1990</b><p><strong>Where it all began.</strong> Challenge Golf starts out at the Family Golf Driving Range in Oakville.</p></div></div><div class="zi r"><div class="zc"><b>1992</b><p><strong>A registered charity.</strong> Golf for the Physically Challenged becomes an officially registered Canadian charity.</p></div></div><div class="zi l"><div class="zc"><b>2013</b><p><strong>A new home at Tee Zone.</strong> We move to Tee Zone Driving Range, owned by BOT Construction, which has generously let us use its range free of charge ever since.</p></div></div><div class="zi r"><div class="zc"><b>2023</b><p><strong>Tournament days.</strong> We launch two annual tournaments at Granite Ridge Golf Club.</p></div></div><div class="zi l"><div class="zc"><b>2024</b><p><strong>Golf all year round.</strong> Our winter indoor program begins at Birdies Indoor Golf in Oakville, making Challenge Golf a year-round program.</p></div></div><div class="zi r"><div class="zc"><b>2024</b><p><strong>A holiday tradition.</strong> We hold our first Christmas gathering, bringing members together for the holiday season.</p></div></div><div class="zi l"><div class="zc"><b>Today</b><p><strong>Still growing.</strong> Weekly summer and winter programs, tournaments, social events and new caregiver support, all run by volunteers. In 2027 we celebrate 35 years. <a href="cg35.html" style="color:var(--red);font-weight:700">Join the celebration →</a></p></div></div></div></div></section>

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
<div class="btns"><a class="btn btn-red" href="contact.html">Arrange a visit</a></div></div></div>'''

page("programs.html", "Programs | Challenge Golf", "Summer, winter, tournaments and caregiver support programs.",
     phero("Programs", "Play all year", "Our weekly programs are free for participants. New participants and volunteers are always welcome to visit a session before deciding to join."),
     f'''<section><div class="wrap">
{pcard("summer","Summer Program","May – early October","Weekly sessions on the driving range and golf course, tailored for people with physical limitations. Volunteers and our golf cart help participants get from the parking lot to our reserved tees.",
 [("When","Mondays, 1:00–2:30 pm (except statutory holidays)"),("Season","Early May to the start of October"),("Where","Tee Zone Driving Range, 4105 Bronte Rd (north of Hwy 407), Oakville"),("Cost","Free")],"summer program at Tee Zone","#e4f2d0")}
{pcard("winter","Winter Program","January – spring","Keep your swing going through the winter on indoor golf simulators, in a warm, relaxed setting with the same friendly volunteers.",
 [("When","Mondays, 1–3 pm"),("Starts","January 11, 2027"),("Where",BIRDIES),("Cost","Free")],"winter program indoors","#e2f0f4")}
{pcard("tournaments","Golf Tournaments","Twice a season","Two tournaments a year at Granite Ridge Golf Club, a chance to get out on the course and enjoy a full day of golf. Each participant is paired with a volunteer.",
 [("Where","Granite Ridge Golf Club"),("How often","Two tournaments each season"),("Format","Groups of four, best ball, double-bogey maximum. Each participant is paired with a volunteer."),("Cost","Subsidized fee")],"golf tournament at Granite Ridge","#e2f0f4")}
{pcard("caregivers","Beyond Caregiving","New in 2026","A support group for caregivers, giving them time, support and a community of their own, led by a professional facilitator.",
 [("When","One 2-hour session a month, Thursdays"),("Where","St. Paul's United Church, Oakville"),("Led by","A professional facilitator"),("Cost","Free")],"caregiver group","#fde9e4")}
<div class="banner green" style="margin-top:40px"><span class="seal"><img src="{LOGO}" alt=""></span><div><h3>Come and visit us first</h3><p>We encourage all new participants and volunteers to come out and visit a session before deciding to join. Spaces are limited, and registration forms are sent out each season, so contact us to arrange a visit.</p></div><a class="btn" href="contact.html">Contact us</a></div>
</div></section>

<section class="white"><div class="wrap split"><div><span class="sec-k">What to expect</span><h2>Your first session</h2>
<ul class="ticks"><li>No golf experience is needed. Volunteers offer advice, tuition and encouragement.</li><li>Clubs and balls are provided, and tees are kept full by volunteers.</li><li>Our golf cart can take you from the parking lot to the reserved tees.</li><li>Participants arrange their own transportation to the site.</li><li>Participants should be able to manage their basic needs independently or with a little help.</li></ul></div>
<div class="rounded" style="height:380px">{photo("volunteer helping at the tee", "x1")}</div></div></section>''')

# ------------------------------------------------------------------ SCHEDULE & EVENTS
def tile(mon, day, wk, title, text="", kind="", id_=""):
    i = f' id="{id_}"' if id_ else ""
    return (f'<div class="tile {kind}"{i}><div class="cal"><small>{mon}</small><b>{day}</b><span>{wk}</span></div>'
            f'<div><h4>{title}</h4>{"<p>"+text+"</p>" if text else ""}</div></div>')

BIRDIES_SHORT = "1–3 pm · Birdies Indoor Golf"
WINTER = [("NOV","30","Mon","Christmas Lunch","12:00 pm · Mandarin Restaurant, 3105 Dundas St W · $25 cash only","special","christmas"),
  ("JAN","11","Mon","Winter program starts",BIRDIES_SHORT,"",""),("JAN","18","Mon","Indoor golf",BIRDIES_SHORT,"",""),("JAN","25","Mon","Indoor golf",BIRDIES_SHORT,"",""),
  ("FEB","1","Mon","Indoor golf",BIRDIES_SHORT,"",""),("FEB","8","Mon","Indoor golf",BIRDIES_SHORT,"",""),("FEB","15","Mon","No golf · Family Day","","off",""),("FEB","22","Mon","Indoor golf",BIRDIES_SHORT,"",""),
  ("MAR","1","Mon","Indoor golf",BIRDIES_SHORT,"",""),("MAR","8","Mon","Indoor golf",BIRDIES_SHORT,"",""),("MAR","15","Mon","Indoor golf",BIRDIES_SHORT,"",""),("MAR","22","Mon","Indoor golf",BIRDIES_SHORT,"",""),("MAR","29","Mon","No golf · Easter Monday","","off",""),
  ("APR","5","Mon","Indoor golf",BIRDIES_SHORT,"",""),("APR","12","Mon","Indoor golf",BIRDIES_SHORT,"",""),
  ("APR","17","Sat","CG35 · 35th Anniversary Celebration","2–9 pm · Oakville Conference Centre · <a class=\"tlink\" href=\"https://ocf.fcsuite.com/erp/donate/list/event?event_date_id=2274\" target=\"_blank\" rel=\"noopener\">Buy tickets →</a>","special","cg35"),
  ("APR","19","Mon","Last day of indoor golf",BIRDIES_SHORT,"","")]

page("events.html", "Schedule & Events | Challenge Golf", "Our winter golf schedule, the Christmas Lunch, the CG35 celebration and other events.",
     phero("Events", "Schedule & events", "Golf dates, social events and celebrations that bring participants, families, volunteers and supporters together all year round."),
     f'''<section><div class="wrap"><span class="sec-k">Winter 2026 – 2027</span><h2>Winter schedule</h2>
<p class="lead">Indoor golf runs Mondays, 1–3 pm, at Birdies Indoor Golf Oakville, 504 Iroquois Shore Rd, Unit 8. <a class="tlink" href="{BIRDIES_MAP}" target="_blank" rel="noopener">Get directions →</a></p>
<div class="tiles">{''.join(tile(*w) for w in WINTER)}</div>
<p class="legend"><span class="k sp"></span>Special event <span class="k"></span>Indoor golf <span class="k off"></span>No golf</p></div></section>

<section class="white"><div class="wrap"><span class="sec-k">More events</span><h2>Throughout the year</h2>
<div class="tiles big">
{tile("NOV","13","to Dec 7","GIVEOakville 2026","We're taking part in the Oakville Community Foundation's giving campaign. Every gift helps keep our programs free.","","give")}
{tile("JUL","TBA","2027","Annual Summer BBQ","Held at Tee Zone Driving Range. The 2026 BBQ was sponsored by Maple Lodge Farms for the third year in a row.","","bbq")}
{tile("AUG","TBA","2027","Golf Tournaments","Two tournaments a season at Granite Ridge Golf Club. In 2026 we played Monday, August 24 and Monday, October 19.","","tournaments")}
{tile("TBA","★","2027","Volunteer Appreciation","A thank-you celebration for our volunteers. A special thank you to Charter Abilities for a wonderful boat ride for our 2026 Volunteer Appreciation.","","volunteers")}
</div></div></section>
<section><div class="wrap center"><h2>See our past events</h2><p class="lead">Photos and videos from tournaments, BBQs and luncheons through the years.</p><a class="btn btn-green" style="margin-top:18px" href="gallery.html">Visit the gallery</a></div></section>''')

# ------------------------------------------------------------------ CG35
page("cg35.html", "CG35 Gala | Challenge Golf 35th Anniversary", "Celebrate 35 years of Challenge Golf on April 17, 2027.",
     f'''<div class="wrap cg-hero"><span class="seal"><img src="{LOGO}" alt="Challenge Golf 35 Years: Believe and Achieve"></span>
<div><span class="kicker">CG35 · 1992–2027</span><h1 style="font-family:var(--serif);font-size:64px;font-weight:400;text-transform:uppercase;line-height:1.02;margin-top:12px">35th Anniversary<br>Celebration</h1>
<p style="font-size:20px;opacity:.9;margin:16px 0 28px">Saturday, April 17, 2027 · 2–9 pm · Oakville Conference Centre</p>
<div class="btns"><a class="btn btn-red" href="https://ocf.fcsuite.com/erp/donate/list/event?event_date_id=2274" target="_blank" rel="noopener">Get tickets</a><a class="btn btn-ghost" href="#sponsor">Become a sponsor</a></div></div></div>''',
     f'''<section><div class="wrap split top-align"><div><span class="sec-k">The celebration</span><h2>Thirty-five years of believing and achieving</h2><div class="prose">
<p>Since 1992, Challenge Golf has helped people living with physical challenges enjoy the game. On April 17, 2027 we're celebrating with the participants, families, volunteers and supporters who made it happen.</p>
<p>Join us for an afternoon and evening of stories, celebration and community, and help us raise funds for the next 35 years.</p></div>

<h3 style="font-family:var(--serif);font-size:24px;font-weight:400;text-transform:uppercase;margin-top:26px;color:var(--green-d)">Highlights</h3>
<ul class="ticks"><li>An exhibition of Challenge Golf's history, with stories from our participants and work by local artists</li><li>The first-ever Richard Malinski Award</li><li>Speeches from board members, participants and local leaders</li></ul>
<p style="margin-top:20px;color:var(--muted)">Special thanks to the <strong style="color:var(--green-d)">Oakville Community Foundation</strong> for their support with ticketing.</p></div>
<div class="ticket" id="tickets"><h3 style="font-family:var(--serif);font-size:28px;font-weight:400;text-transform:uppercase;margin-bottom:10px">Event details</h3>
<div class="row"><span>Date</span><b>Saturday, April 17, 2027</b></div><div class="row"><span>Time</span><b>2:00 – 9:00 pm</b></div>
<div class="row"><span>Venue</span><b>Oakville Conference Centre<br><small style="font-weight:500;color:var(--muted)">2515 Wyecroft Rd, Oakville</small></b></div><div class="row" style="border-bottom:0"><span>Schedule</span><b></b></div><div class="sched"><div><b>2:00 – 4:00 pm</b><span>Reception, exhibition &amp; souvenirs</span></div><div><b>4:00 – 5:30 pm</b><span>Richard Malinski Award, speeches &amp; live music by members of the Oakville Symphony Orchestra</span></div><div><b>5:30 pm onward</b><span>Three-course dinner &amp; dance</span></div></div><div class="row"><span>Tickets</span><b>$100 per person</b></div><div class="row"><span>On sale until</span><b>April 2, 2027</b></div>
<p style="font-size:14.5px;color:var(--muted);margin-top:14px">Your ticket includes the reception, a souvenir, a performance by musicians from the Oakville Symphony Orchestra, and a three-course dinner &amp; dance.</p>
<a class="btn btn-red" href="https://ocf.fcsuite.com/erp/donate/list/event?event_date_id=2274" target="_blank" rel="noopener" style="display:block;text-align:center;margin-top:18px">Buy tickets</a></div></div></section>

<section class="white" id="sponsor"><div class="wrap"><span class="sec-k">Sponsorship</span><h2>Sponsor CG35</h2><p class="lead">Help us celebrate 35 years of changing lives through golf. Your sponsorship also helps cover costs for participants facing financial difficulties, so cost never becomes a barrier to taking part.</p>
<div class="tiers t5" style="margin-top:30px">
<div class="tier"><small>1 available</small><b>Presenting Sponsor</b><em>$8,000</em><p>On-stage mention, prominent logo display, 8 tickets</p></div>
<div class="tier"><small>1 available</small><b>Gold</b><em>$5,000</em><p>Logo throughout the exhibition area, 4 tickets</p></div>
<div class="tier"><small>1 available</small><b>Silver</b><em>$3,000</em><p>Logo at the reception area, 2 tickets</p></div>
<div class="tier"><small>&nbsp;</small><b>Table Sponsor</b><em>$1,000</em><p>Logo on a table centrepiece, 2 tickets</p></div>
<div class="tier"><small>&nbsp;</small><b>Community Sponsor</b><em>$500</em><p>Recognition on our website and social media</p></div></div>
<p style="color:var(--muted);margin-top:20px">All sponsors are recognized on our website and social media. We're happy to work with you to shape a sponsorship that fits your organization.</p>
<div class="btns" style="margin-top:22px"><a class="btn btn-red" href="contact.html">Enquire about sponsorship</a><a class="btn btn-green" href="mailto:{EMAIL}?subject=CG35%20sponsorship">Email {EMAIL}</a></div></div></section>

<section><div class="wrap"><span class="sec-k">35 years in pictures</span><h2>Our community today</h2>
<div class="grid3">{photo("indoor swing","c1",h="280px")}{photo("bbq friends","c2",h="280px")}{photo("community social","c3",h="280px")}</div></div></section>''')

# ------------------------------------------------------------------ GALLERY
GALLERY = ['img/photos/course-cart', 'img/photos/simulator-lesson', 'img/photos/putting-green-four', 'img/photos/range-lineup', 'img/photos/tournament-five', 'img/photos/bbq-overview', 'img/photos/bbq-table', 'img/photos/boat-group', 'img/photos/boat-help', 'img/photos/boat-wave', 'img/photos/caregiver-chat', 'img/photos/cart-friends', 'img/photos/christmas-friends', 'img/photos/christmas-room', 'img/photos/civitan-cheque', 'img/photos/coaching-arm', 'img/photos/flag-friends', 'img/photos/group-lanai', 'img/photos/group-teezone', 'img/photos/hero-friends', 'img/photos/high-five', 'img/photos/hug', 'img/photos/indoor-group', 'img/photos/maple-lodge', 'img/photos/opening-day', 'img/photos/patio-friends', 'img/photos/putting-brace', 'img/photos/range-laughs', 'img/photos/range-powerchair', 'img/photos/range-smiles', 'img/photos/summer-patio2', 'img/photos/swing-follow', 'img/photos/team-friends', 'img/photos/teezone-patio', 'img/photos/tournament-adaptive', 'img/photos/tournament-colour', 'img/photos/tournament-peace', 'img/photos/volunteers-gazebo', 'img/photos/winter-coaching', 'img/photos/winter-lounge', 'img/photos/winter-ramp', 'img/photos/winter-stool', 'img/photos/winter-team', 'img/photos/winter-volunteers', 'img/gallery/cg-001', 'img/gallery/cg-002', 'img/gallery/cg-003', 'img/gallery/cg-004', 'img/gallery/cg-005', 'img/gallery/cg-006', 'img/gallery/cg-007', 'img/gallery/cg-008', 'img/gallery/cg-009', 'img/gallery/cg-015', 'img/gallery/cg-016', 'img/gallery/cg-017', 'img/gallery/cg-020', 'img/gallery/cg-021', 'img/gallery/cg-022', 'img/gallery/cg-025', 'img/gallery/cg-027', 'img/gallery/cg-028', 'img/gallery/cg-029', 'img/gallery/cg-032', 'img/gallery/cg-033', 'img/gallery/cg-035', 'img/gallery/cg-037', 'img/gallery/cg-038', 'img/gallery/cg-040', 'img/gallery/cg-041', 'img/gallery/cg-046', 'img/gallery/cg-047', 'img/gallery/cg-050', 'img/gallery/cg-052', 'img/gallery/cg-053', 'img/gallery/cg-054', 'img/gallery/cg-055', 'img/gallery/cg-058', 'img/gallery/cg-059', 'img/gallery/cg-061', 'img/gallery/cg-062', 'img/gallery/cg-069', 'img/gallery/cg-070', 'img/gallery/cg-074', 'img/gallery/cg-077', 'img/gallery/cg-084', 'img/gallery/cg-085', 'img/gallery/cg-086', 'img/gallery/cg-098', 'img/gallery/cg-100', 'img/gallery/cg-101', 'img/gallery/cg-104', 'img/gallery/cg-105', 'img/gallery/cg-106', 'img/gallery/cg-108', 'img/gallery/cg-109', 'img/gallery/cg-110', 'img/gallery/cg-117', 'img/gallery/cg-121', 'img/gallery/cg-125', 'img/gallery/cg-126', 'img/gallery/cg-127', 'img/gallery/cg-131', 'img/gallery/cg-134', 'img/gallery/cg-137', 'img/gallery/cg-138', 'img/gallery/cg-159']
albums = [("Summer Program", "Mondays at Tee Zone", "#e4f2d0"), ("Golf Tournaments", "Granite Ridge, 2023–2025", "#e2f0f4"),
          ("Annual BBQ", "Thanks to Maple Lodge Farms", "#fde9e4"), ("Christmas Luncheon album", "Festive gatherings", "#fde9e4"),
          ("Winter Program", "Indoor simulators", "#e2f0f4"), ("Volunteer Appreciation", "Thank-you cruise, 2026", "#eef6dc")]
page("gallery.html", "Gallery | Challenge Golf", "Photos and videos from Challenge Golf programs and events.",
     phero("Gallery", "Moments on the course", "Photos and videos from our programs, tournaments and celebrations."),
     f'''<section><div class="wrap"><span class="sec-k">In the news</span><h2>Challenge Golf on video</h2><div class="grid2">
<div class="vid"><a class="video" href="https://youtu.be/fzcwRyUzTF8" data-yt="fzcwRyUzTF8" aria-label="Play video: YourTV feature on Challenge Golf"><img src="img/photos/range-laughs.jpg" alt="Participants laughing on the range"><span class="play" aria-hidden="true">▶</span><span class="cap">YourTV (Cogeco)</span></a>
<h3>YourTV visits Challenge Golf</h3><p>YourTV, Cogeco's community channel, spent a day with our participants and volunteers to share how golf builds confidence, friendship and community.</p></div>
<div class="vid"><a class="video" href="https://youtu.be/tVcAj_22jJY" data-yt="tVcAj_22jJY" aria-label="Play video: The Hamilton Spectator on Challenge Golf"><img src="img/photos/summer-patio2.jpg" alt="Members on the Tee Zone patio"><span class="play" aria-hidden="true">▶</span><span class="cap">The Hamilton Spectator</span></a>
<h3>The Hamilton Spectator</h3><p>The Hamilton Spectator's video story on Challenge Golf and the people who make our program what it is.</p></div>
</div></div></section>
<section style="padding-top:0"><div class="wrap"><span class="sec-k">Photos</span><h2>Our community in pictures</h2>
<div class="pgrid">{''.join(f'<a href="{f}.jpg" target="_blank" rel="noopener"><img src="{f}.jpg" alt="Challenge Golf photo" loading="lazy" decoding="async"></a>' for f in GALLERY)}</div>
<p style="color:var(--muted);margin-top:18px">Have photos from a Challenge Golf event? Send them to <a href="mailto:{EMAIL}" style="color:var(--red);font-weight:700">{EMAIL}</a>.</p></div></section>''')

# ------------------------------------------------------------------ SUPPORT US
sponsors = [("tee-zone", "Tee Zone Driving Range"), ("granite-ridge", "Granite Ridge Golf Club"), ("birdies-indoor-golf", "Birdies Indoor Golf"),
            ("civitan-oakville", "Civitan Club of Oakville"), ("paragolf-ontario", "Paragolf Ontario"), ("golf-journalists", "Golf Journalists Association of Canada"),
            ("golf-canada-foundation", "Golf Canada Foundation"), ("enbridge", "Enbridge Fueling Futures"), ("mind-forward", "Mind Forward Brain Injury Services"),
            ("passion-for-parkinsons", "Passion for Parkinson's Foundation"), ("oakville-strokers", "Oakville Strokers"), ("maple-lodge-farms", "Maple Lodge Farms"),
            ("oakville-community-foundation", "Oakville Community Foundation"), ("canadian-women-sport", "Canadian Women & Sport")]
icon = lambda p: f'<span class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#25502a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg></span>'
page("support.html", "Support Us | Challenge Golf", "Donate, volunteer, sponsor or donate golf equipment.",
     phero("Support us", "Help every golfer swing", "Challenge Golf is run entirely by volunteers, so every donation goes directly to our programs."),
     f'''<section><div class="wrap"><div class="help">
<a href="#donate">{icon('<path d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z"/>')}<h3>Donate</h3><p>Instant tax receipts for every gift.</p></a>
<a href="#volunteer">{icon('<circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2M16 3.1a4 4 0 0 1 0 7.8M21 21v-2a4 4 0 0 0-3-3.9"/>')}<h3>Volunteer</h3><p>Join us at the range on Mondays.</p></a>
<a href="#sponsor">{icon('<path d="M12 2l3 6.5 7 .8-5.2 4.8 1.4 7L12 17.8 5.8 21.1l1.4-7L2 9.3l7-.8z"/>')}<h3>Sponsor</h3><p>Partner with us on events and CG35.</p></a>
<a href="#equipment">{icon('<path d="M8 3v14"/><path d="M8 3l8 3-8 3"/><circle cx="15" cy="19" r="2.5"/>')}<h3>Donate equipment</h3><p>Clubs, balls, bags and accessories.</p></a>
</div></div></section>

<section class="white" id="donate"><div class="wrap"><div class="center" style="max-width:760px;margin:0 auto"><span class="sec-k">Donate</span><h2>Make a donation</h2>
<p class="lead">Challenge Golf is <strong style="color:var(--green-d)">100% volunteer-run</strong>, so every donation goes directly toward our programs and events.</p></div>
<h3 class="dh">Your donation helps us</h3>
<div class="why four"><div><b>Keep our programs free</b><span>No fees for participants in our weekly programs.</span></div>
<div><b>Buy adaptive equipment</b><span>Clubs and equipment suited to each participant's abilities.</span></div>
<div><b>Remove cost as a barrier</b><span>Subsidize or cover tournament and social event costs for participants facing financial difficulties.</span></div>
<div><b>Run our programs and events</b><span>With no paid staff, your gift goes straight to the golf, the events and the people.</span></div></div>
<div class="dA">
<a class="pc" href="https://www.canadahelps.org/en/dn/92488" target="_blank" rel="noopener"><h3>CanadaHelps</h3><p>Canada's largest online giving platform. Give once or monthly, with an instant tax receipt.</p><span class="btn btn-red">Donate on CanadaHelps</span></a>
<a class="pc" href="https://www.zeffy.com/en-CA/donation-form/donate-to-help-empower-the-lives-of-people-living-with-physical-limitations-through-golf" target="_blank" rel="noopener"><h3>Zeffy</h3><p>A free donation platform for charities, so more of your gift reaches our programs. Instant tax receipt.</p><span class="btn btn-green">Donate on Zeffy</span></a></div>
<p class="center" style="color:var(--muted);font-size:14.5px;margin-top:16px">Challenge Golf is a registered Canadian charity ({CHARITY}). Both links open a secure donation page in a new tab.</p></div></section>

<section id="volunteer"><div class="wrap split"><div class="rounded" style="height:420px">{photo("volunteers at Tee Zone", "v1")}</div>
<div><span class="sec-k">Volunteer</span><h2>Be part of the team</h2><p class="lead">Volunteers create a friendly, safe and encouraging environment for our participants. No golf expertise is needed, just a willingness to help and get to know people.</p>
<div class="btns"><a class="btn btn-red" href="contact.html">I'd like to volunteer</a></div>
<p style="color:var(--muted);font-size:15px;margin-top:12px">Or drop by and say hello at a Monday session.</p></div></div></section>

<section class="white" id="equipment"><div class="wrap split"><div><span class="sec-k">Equipment</span><h2>Donate your golf clubs</h2>
<p class="lead">We welcome new or gently used golf clubs, balls, bags, grips and other accessories. At the moment we can only accept donations in and around the Halton and Peel regions.</p>
<div class="btns" style="margin-top:24px"><a class="btn btn-green" href="contact.html">Arrange a drop-off</a></div></div>
<div id="sponsor" class="card r" style="padding:36px"><span class="sec-k">Sponsor</span><h3 style="font-family:var(--serif);font-size:30px;font-weight:400;text-transform:uppercase;margin-top:6px">Partner with us</h3>
<p>Support our tournaments, BBQ, Christmas Luncheon or the CG35 celebration, and be recognized on our website, on our social media and at events.</p><a class="btn btn-red" href="contact.html">Sponsorship enquiries</a></div></div></section>

<section id="supporters"><div class="wrap center"><span class="sec-k">Thank you</span><h2>Our supporters</h2><p class="lead">Thank you to every organization that helps keep Challenge Golf free for participants. Our recent supporters have included:</p>
<div class="logos" style="margin-top:30px">{''.join(f'<div><img src="img/sponsors/{s}.png" alt="{n}" title="{n}"></div>' for s,n in sponsors)}</div></div></section>''')

# ------------------------------------------------------------------ CONTACT
page("contact.html", "Contact Us | Challenge Golf", "Get in touch with Challenge Golf. Email info@challengegolf.ca.",
     phero("Contact", "We'd love to hear from you", "Questions about programs, volunteering, sponsorship or donations? Send us a message."),
     f'''<section><div class="wrap split top-align"><div>
<div class="info"><div><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div><small>Summer program location</small>Tee Zone Driving Range<br>4105 Bronte Road (north of Hwy 407), Oakville, ON<br><a href="https://maps.google.com/?q=Tee+Zone+Driving+Range+4105+Bronte+Road+Oakville" target="_blank" rel="noopener" style="color:var(--red);font-weight:700">Get directions to Tee Zone →</a></div>
<div><small>Winter program location</small>{BIRDIES}<br><a href="{BIRDIES_MAP}" target="_blank" rel="noopener" style="color:var(--red);font-weight:700">Get directions to Birdies →</a></div>
<div class="soc"><small>Follow us</small>{SOCIAL}</div></div>
</div>
<div class="ticket"><h3 style="font-family:var(--serif);font-size:28px;font-weight:400;text-transform:uppercase;margin-bottom:16px">Send a message</h3>
<form action="https://formsubmit.co/{EMAIL}" method="POST">
<input type="hidden" name="_subject" value="New message from the Challenge Golf website"><input type="hidden" name="_template" value="table"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<div class="f2"><label><span class="sr">Your name</span><input class="f" name="name" placeholder="Your name" required autocomplete="name"></label><label><span class="sr">Email</span><input class="f" type="email" name="email" placeholder="Email" required autocomplete="email"></label></div>
<label><span class="sr">Phone (optional)</span><input class="f" type="tel" name="phone" placeholder="Phone (optional)" autocomplete="tel"></label>
<label><span class="sr">I'm interested in</span><select class="f" name="interest"><option value="">I'm interested in…</option><option>Visiting / joining a program</option><option>Volunteering</option><option>Sponsoring</option><option>Donating</option><option>Other</option></select></label>
<label><span class="sr">Message</span><textarea class="f tall" name="message" placeholder="Message" required></textarea></label>
<button class="btn btn-red" type="submit" style="justify-self:start">Send message</button></form></div></div></section>''')


# ------------------------------------------------------------------ MEMBERS (draft, not in menu yet)
FORM_ID = "1W03fyI15km5hQTgJby1a8CuAzfboky9HZQLtFWnPSYo"
FORM_VIEW = f"https://docs.google.com/forms/d/{FORM_ID}/viewform"
page("members.html", "Members | Challenge Golf", "Registration and sign-ups for Challenge Golf participants and volunteers.",
     phero("Members", "Member hub", "Registration, sign-ups and key dates for Challenge Golf participants and volunteers, all in one place."),
     f'''<section><div class="wrap">
<div class="tiles big mtiles">
{tile("JAN","11","Mon","Winter Program 2027","Mondays, 1–3 pm, Jan 11 – Apr 19 at Birdies Indoor Golf Oakville. <b>Registration open below.</b>","special","")}
{tile("MAY","TBA","2027","Summer Program 2027","Registration to be announced.","","")}
{tile("AUG","23","Mon","Tournament #1","Granite Ridge Golf Club · first tee 10:00 am. Registration opens in the summer.","","")}
{tile("OCT","18","Mon","Tournament #2","Granite Ridge Golf Club · first tee 10:00 am. Registration opens in the summer.","","")}
{tile("NOV","30","Mon","Christmas Lunch","12:00 pm · Mandarin Restaurant, 3105 Dundas St W · $25 cash only","","")}
{tile("TBD","★","2027","Summer BBQ","Date to be determined.","off","")}
{tile("TBD","★","2027","Volunteer Appreciation","Date to be determined.","off","")}
</div></div></section>

<section class="white" id="winter-registration"><div class="wrap"><div class="center" style="max-width:760px;margin:0 auto">
<span class="sec-k">Now open</span><h2>2027 Winter Program Registration</h2>
<p class="lead">For participants and volunteers. Mondays, 1–3 pm, January 11 to April 19, 2027 at Birdies Indoor Golf Oakville, 504 Iroquois Shore Rd, Unit 8. No Google account is needed to register.</p></div>
<div class="formbox"><iframe src="{FORM_VIEW}?embedded=true" title="2027 Winter Program Registration - Challenge Golf" loading="lazy">Loading…</iframe></div>
<p class="center" style="margin-top:14px;color:var(--muted)">Having trouble with the form? <a class="tlink" href="{FORM_VIEW}" target="_blank" rel="noopener">Open it in a new tab →</a> or email <a class="tlink" href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>

<section><div class="wrap"><div class="grid2">
<div class="card"><h3>Summer Program 2027</h3><p>Registration will be announced in the spring. Watch your email or check back here.</p><div class="m">Tee Zone Driving Range · Mondays</div></div>
<div class="card g"><h3>2027 Tournaments</h3><p>Monday, August 23 and Monday, October 18 at Granite Ridge Golf Club, first tee 10:00 am. Groups of four, best ball, each participant paired with a volunteer. Registration opens in the summer.</p><div class="m">Subsidized fee</div></div>
</div></div></section>''',
     extra_head='<meta name="robots" content="noindex, nofollow">')

print("built", [f for f in os.listdir(OUT) if f.endswith(".html")])
