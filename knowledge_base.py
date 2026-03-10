# =========================
# Knowledge Base
# =========================


from inference_engine import defrule

# =========================
# Stop message
# =========================

STOP_MESSAGE = (
    "Please seek guidance from an appropriate allied health professional "
    "or medical practitioner prior to undertaking exercise."
)

# =========================
# APSS Questions
# =========================

APSS_QUESTIONS = [
    ("apss1", "Do you have any medical conditions that limit physical activity?"),
    ("apss2", "Have you ever suffered a heart condition or been told you have a heart condition?"),
    ("apss3", "Do you ever experience unexpected pains or discomfort in your chest at rest or during physical activity?"),
    ("apss4", "Do you ever lose balance because of dizziness or have you lost consciousness (fainted)?"),
    ("apss5", "Do you have any bone, joint or muscle problems that could be made worse by exercise?"),
    ("apss6", "Is your doctor currently prescribing medication for your blood pressure or a heart condition?"),
]

# =========================
# Activity Descriptions
# =========================

ACTIVITY_DESC = {
    "Running":               "Improves cardiovascular health and endurance. Intensity can be adjusted (easy runs, intervals, hill sprints).",
    "Hiking":                "Low-impact outdoor activity that builds endurance and burns calories. Needs minimal equipment.",
    "Yoga":                  "Improves flexibility, balance, and posture while reducing stress through controlled movement and breathing.",
    "Cycling":               "Improves cardiovascular fitness and leg strength. Can be done outdoors or on a stationary bike.",
    "Swimming":              "Low-impact, full-body exercise that improves endurance and muscular strength while being gentle on joints.",
    "Treadmill Run":         "Gives similar benefits to outdoor running while letting you control pace and monitor distance and calories.",
    "Outdoor Rock Climbing": "Builds strength and strength-endurance, plus focus and a sense of adventure.",
    "Indoor Rock Climbing":  "Develops physical strength and endurance while improving problem-solving and focus in a controlled setting.",
    "Weight Training":       "Builds muscular strength and can be progressed over time by increasing resistance and volume.",
    "Team sport":            "Fun social workouts (e.g. football/basketball) that build fitness, teamwork, and communication.",
    "Tai Chi":               "Low-impact practice that supports balance, mobility, and calm focus, often done in groups.",
    "Pilates":               "Strengthens core muscles and improves posture and flexibility, supporting better movement control.",
    "Circuit Training":      "Mixes multiple exercises with short rests to build endurance and strength in a time-efficient way.",
    "Aerobics":              "Rhythmic group workout that improves cardiovascular fitness and burns calories.",
    "Dancing Class":         "Improves cardio fitness and coordination while being enjoyable and motivating in a group.",
    "Rowing":                "Builds cardiovascular endurance and full-body strength, using legs, core, and upper body.",
    "Calisthenics":          "Uses bodyweight movements to build strength and control (push-ups, pull-ups, squats).",
    "Boxing":                "Improves strength, coordination, and cardiovascular fitness; a strong full-body workout.",
}

# =========================
# Rules
# =========================

# ── APSS Screenig ────────────────────────────

defrule("APSS_STOP_1", [("apss1", "yes")], [("stop", "true")])
defrule("APSS_STOP_2", [("apss2", "yes")], [("stop", "true")])
defrule("APSS_STOP_3", [("apss3", "yes")], [("stop", "true")])
defrule("APSS_STOP_4", [("apss4", "yes")], [("stop", "true")])
defrule("APSS_STOP_5", [("apss5", "yes")], [("stop", "true")])
defrule("APSS_STOP_6", [("apss6", "yes")], [("stop", "true")])

defrule("APSS_CLEARED",
    [("apss1","no"),("apss2","no"),("apss3","no"),("apss4","no"),("apss5","no"),("apss6","no")],
    [("screen", "cleared")])


# ── Mode ────────────────────────────


defrule("MODE_SOLO",  [("screen","cleared"),("mode","On my own")],   [("solo","true")])
defrule("MODE_GROUP", [("screen","cleared"),("mode","Group-based")], [("group","true")])


# ── Goal ───────────────────────────

# Solo 
defrule("GOAL_SOLO_HEALTHY",  [("solo","true"),("goal","Stay healthy")],   [("goal_mode","solo_healthy")])
defrule("GOAL_SOLO_LOSE",     [("solo","true"),("goal","Lose weight/fat")],[("goal_mode","solo_lose")])
defrule("GOAL_SOLO_STRENGTH", [("solo","true"),("goal","Gain strength")],  [("goal_mode","solo_strength")])

# Group 
defrule("GOAL_GRP_HEALTHY",   [("group","true"),("goal","Stay healthy")],   [("goal_mode","grp_healthy")])
defrule("GOAL_GRP_LOSE",      [("group","true"),("goal","Lose weight/fat")],[("goal_mode","grp_lose")])
defrule("GOAL_GRP_STRENGTH",  [("group","true"),("goal","Gain strength")],  [("goal_mode","grp_strength")])


# ── Environment ─────────────────────────


# Solo / healthy
defrule("PROFILE_SOLO_HEALTHY_OUTDOOR", [("goal_mode","solo_healthy"),  ("env","Outdoor")], [("profile","own_healthy_outdoor")])
defrule("PROFILE_SOLO_HEALTHY_INDOOR",  [("goal_mode","solo_healthy"),  ("env","Indoor")],  [("profile","own_healthy_indoor")])
defrule("PROFILE_SOLO_HEALTHY_EITHER",  [("goal_mode","solo_healthy"),  ("env","Either")],  [("profile","own_healthy_either")])

# Solo / lose weight
defrule("PROFILE_SOLO_LOSE_OUTDOOR",    [("goal_mode","solo_lose"),     ("env","Outdoor")], [("profile","own_lose_outdoor")])
defrule("PROFILE_SOLO_LOSE_INDOOR",     [("goal_mode","solo_lose"),     ("env","Indoor")],  [("profile","own_lose_indoor")])
defrule("PROFILE_SOLO_LOSE_EITHER",     [("goal_mode","solo_lose"),     ("env","Either")],  [("profile","own_lose_either")])

# Solo / strength
defrule("PROFILE_SOLO_STR_OUTDOOR",     [("goal_mode","solo_strength"), ("env","Outdoor")], [("profile","own_str_outdoor")])
defrule("PROFILE_SOLO_STR_INDOOR",      [("goal_mode","solo_strength"), ("env","Indoor")],  [("profile","own_str_indoor")])
defrule("PROFILE_SOLO_STR_EITHER",      [("goal_mode","solo_strength"), ("env","Either")],  [("profile","own_str_either")])

# Group / healthy
defrule("PROFILE_GRP_HEALTHY_OUTDOOR",  [("goal_mode","grp_healthy"),   ("env","Outdoor")], [("profile","grp_healthy_outdoor")])
defrule("PROFILE_GRP_HEALTHY_INDOOR",   [("goal_mode","grp_healthy"),   ("env","Indoor")],  [("profile","grp_healthy_indoor")])
defrule("PROFILE_GRP_HEALTHY_EITHER",   [("goal_mode","grp_healthy"),   ("env","Either")],  [("profile","grp_healthy_either")])

# Group / lose weight
defrule("PROFILE_GRP_LOSE_OUTDOOR",     [("goal_mode","grp_lose"),      ("env","Outdoor")], [("profile","grp_lose_outdoor")])
defrule("PROFILE_GRP_LOSE_INDOOR",      [("goal_mode","grp_lose"),      ("env","Indoor")],  [("profile","grp_lose_indoor")])
defrule("PROFILE_GRP_LOSE_EITHER",      [("goal_mode","grp_lose"),      ("env","Either")],  [("profile","grp_lose_either")])

# Group / strength
defrule("PROFILE_GRP_STR_OUTDOOR",      [("goal_mode","grp_strength"),  ("env","Outdoor")], [("profile","grp_str_outdoor")])
defrule("PROFILE_GRP_STR_INDOOR",       [("goal_mode","grp_strength"),  ("env","Indoor")],  [("profile","grp_str_indoor")])
defrule("PROFILE_GRP_STR_EITHER",       [("goal_mode","grp_strength"),  ("env","Either")],  [("profile","grp_str_either")])


# ── Recommendation ──────────────────────────────────

# own_healthy
defrule("REC_OWN_HEALTHY_OUTDOOR_SHORT", [("profile","own_healthy_outdoor"),("time","<75")],  [("recommend","Running")])
defrule("REC_OWN_HEALTHY_OUTDOOR_LONG",  [("profile","own_healthy_outdoor"),("time",">=75")], [("recommend","Hiking")])
defrule("REC_OWN_HEALTHY_INDOOR_SHORT",  [("profile","own_healthy_indoor"), ("time","<75")],  [("recommend","Yoga")])
defrule("REC_OWN_HEALTHY_INDOOR_LONG",   [("profile","own_healthy_indoor"), ("time",">=75")], [("recommend","Yoga")])
defrule("REC_OWN_HEALTHY_EITHER_SHORT",  [("profile","own_healthy_either"), ("time","<75")],  [("recommend","Running"),("recommend","Yoga")])
defrule("REC_OWN_HEALTHY_EITHER_LONG",   [("profile","own_healthy_either"), ("time",">=75")], [("recommend","Hiking"),("recommend","Yoga")])

# own_lose
defrule("REC_OWN_LOSE_OUTDOOR_SHORT", [("profile","own_lose_outdoor"),("time","<75")],  [("recommend","Running")])
defrule("REC_OWN_LOSE_OUTDOOR_LONG",  [("profile","own_lose_outdoor"),("time",">=75")], [("recommend","Cycling")])
defrule("REC_OWN_LOSE_INDOOR_SHORT",  [("profile","own_lose_indoor"), ("time","<75")],  [("recommend","Treadmill Run")])
defrule("REC_OWN_LOSE_INDOOR_LONG",   [("profile","own_lose_indoor"), ("time",">=75")], [("recommend","Swimming")])
defrule("REC_OWN_LOSE_EITHER_SHORT",  [("profile","own_lose_either"), ("time","<75")],  [("recommend","Running")])
defrule("REC_OWN_LOSE_EITHER_LONG",   [("profile","own_lose_either"), ("time",">=75")], [("recommend","Cycling"),("recommend","Swimming")])

# own_str
defrule("REC_OWN_STR_OUTDOOR_SHORT", [("profile","own_str_outdoor"),("time","<75")],  [("recommend","Outdoor Rock Climbing")])
defrule("REC_OWN_STR_OUTDOOR_LONG",  [("profile","own_str_outdoor"),("time",">=75")], [("recommend","Outdoor Rock Climbing")])
defrule("REC_OWN_STR_INDOOR_SHORT",  [("profile","own_str_indoor"), ("time","<75")],  [("recommend","Weight Training")])
defrule("REC_OWN_STR_INDOOR_LONG",   [("profile","own_str_indoor"), ("time",">=75")], [("recommend","Indoor Rock Climbing"),("recommend","Weight Training")])
defrule("REC_OWN_STR_EITHER_SHORT",  [("profile","own_str_either"), ("time","<75")],  [("recommend","Weight Training"),("recommend","Outdoor Rock Climbing")])
defrule("REC_OWN_STR_EITHER_LONG",   [("profile","own_str_either"), ("time",">=75")], [("recommend","Indoor Rock Climbing"),("recommend","Weight Training"),("recommend","Outdoor Rock Climbing")])

# grp_healthy
defrule("REC_GRP_HEALTHY_OUTDOOR_SHORT", [("profile","grp_healthy_outdoor"),("time","<75")],  [("recommend","Team sport"),("recommend","Tai Chi")])
defrule("REC_GRP_HEALTHY_OUTDOOR_LONG",  [("profile","grp_healthy_outdoor"),("time",">=75")], [("recommend","Team sport"),("recommend","Tai Chi")])
defrule("REC_GRP_HEALTHY_INDOOR_SHORT",  [("profile","grp_healthy_indoor"), ("time","<75")],  [("recommend","Pilates"),("recommend","Circuit Training")])
defrule("REC_GRP_HEALTHY_INDOOR_LONG",   [("profile","grp_healthy_indoor"), ("time",">=75")], [("recommend","Aerobics"),("recommend","Circuit Training"),("recommend","Pilates")])
defrule("REC_GRP_HEALTHY_EITHER_SHORT",  [("profile","grp_healthy_either"), ("time","<75")],  [("recommend","Team sport"),("recommend","Tai Chi"),("recommend","Pilates")])
defrule("REC_GRP_HEALTHY_EITHER_LONG",   [("profile","grp_healthy_either"), ("time",">=75")], [("recommend","Team sport"),("recommend","Tai Chi"),("recommend","Aerobics")])

# grp_lose
defrule("REC_GRP_LOSE_OUTDOOR_SHORT", [("profile","grp_lose_outdoor"),("time","<75")],  [("recommend","Team sport")])
defrule("REC_GRP_LOSE_OUTDOOR_LONG",  [("profile","grp_lose_outdoor"),("time",">=75")], [("recommend","Team sport")])
defrule("REC_GRP_LOSE_INDOOR_SHORT",  [("profile","grp_lose_indoor"), ("time","<75")],  [("recommend","Dancing Class")])
defrule("REC_GRP_LOSE_INDOOR_LONG",   [("profile","grp_lose_indoor"), ("time",">=75")], [("recommend","Aerobics"),("recommend","Dancing Class")])
defrule("REC_GRP_LOSE_EITHER_SHORT",  [("profile","grp_lose_either"), ("time","<75")],  [("recommend","Dancing Class"),("recommend","Team sport")])
defrule("REC_GRP_LOSE_EITHER_LONG",   [("profile","grp_lose_either"), ("time",">=75")], [("recommend","Aerobics"),("recommend","Team sport")])

# grp_str
defrule("REC_GRP_STR_OUTDOOR_SHORT", [("profile","grp_str_outdoor"),("time","<75")],  [("recommend","Rowing"),("recommend","Calisthenics")])
defrule("REC_GRP_STR_OUTDOOR_LONG",  [("profile","grp_str_outdoor"),("time",">=75")], [("recommend","Rowing"),("recommend","Calisthenics")])
defrule("REC_GRP_STR_INDOOR_SHORT",  [("profile","grp_str_indoor"), ("time","<75")],  [("recommend","Boxing"),("recommend","Circuit Training")])
defrule("REC_GRP_STR_INDOOR_LONG",   [("profile","grp_str_indoor"), ("time",">=75")], [("recommend","Boxing"),("recommend","Circuit Training"),("recommend","Pilates")])
defrule("REC_GRP_STR_EITHER_SHORT",  [("profile","grp_str_either"), ("time","<75")],  [("recommend","Boxing"),("recommend","Rowing"),("recommend","Calisthenics")])
defrule("REC_GRP_STR_EITHER_LONG",   [("profile","grp_str_either"), ("time",">=75")], [("recommend","Circuit Training"),("recommend","Rowing"),("recommend","Calisthenics")])