"""
hungary_signal_interpreter.py
Asifah Analytics -- Europe Backend Module
v1.0.0 -- May 17, 2026

HUNGARY SIGNAL INTERPRETER

Converts rhetoric_tracker_hungary scan output into analytical product:
red lines + green lines + diplomatic track + so-what + historical matches.

PRIMARY ANALYTICAL FRAME: AXIS REVERSAL
  Hungary is the first documented EU member country undergoing a democratic
  axis reversal from Russia-dependent to EU-aligned posture, following the
  April 2026 Tisza landslide defeat of Orban/Fidesz. This interpreter watches
  for: (a) durability of the reversal, (b) Orban/Fidesz counter-signals,
  (c) Russia counter-pressure on Hungary.

RED LINES (5):
  1. axis_reversal_in_progress      [diplomatic_signal]   severity 2
  2. orban_revival_signal           [diplomatic_signal]   severity 3
  3. eu_loan_unlock_active          [diplomatic_signal]   severity 1
  4. druzhba_pipeline_dispute       [economic_signal]     severity 2
  5. seized_assets_returned         [diplomatic_signal]   severity 1

KEY DESIGN DECISION:
  Red lines are tagged with pressure_type so GPI's classifier routes them
  to the correct axis. axis-reversal-in-progress -> Diplomatic axis (the
  primary intent). druzhba pipeline -> Economic axis (resource flow).

EMITS pressure_type tags compatible with GPI axis classifier:
  - 'diplomatic' for reversal/election/sovereignty signals
  - 'economic'   for pipeline/contract/sanctions signals

Author: RCGG / Asifah Analytics
"""
from datetime import datetime, timezone


# ============================================================
# RED LINES (canonical structure mirrors Russia interpreter)
# ============================================================
RED_LINES = [

    # ── Category A: AXIS REVERSAL (Diplomatic axis) ─────────────
    {
        'id':       'axis_reversal_in_progress',
        'label':    'Hungary Axis Reversal In Progress',
        'detail':   'Multiple symptoms of Russia-axis dependency unwinding '
                    'simultaneously: returned seized assets + EU loan veto '
                    'lifted + Druzhba flow resumed + pro-EU statements from '
                    'new government. The analytical heart of the Hungary case.',
        'severity':       2,
        'color':          '#3b82f6',
        'icon':           '🪜',
        'category':       'diplomatic_signal',
        'pressure_type':  'diplomatic',
        'source':         'AP/Spike May 6 2026 + April 2026 Tisza election + '
                          'EU loan unlock reporting + Druzhba pipeline resumption. '
                          'Hungary is the first documented Russia-axis-dependent '
                          'EU member to undergo democratic axis reversal that '
                          'Asifah can track in real-time.',
    },

    # ── Category B: OPPOSITION COUNTER-PRESSURE (Diplomatic axis) ──
    {
        'id':       'orban_revival_signal',
        'label':    'Orban / Fidesz Revival Signal',
        'detail':   'Orban and Fidesz pursuing political comeback through '
                    'Putin/Trump direct lines, mass rallies, anti-Ukraine '
                    'messaging revival, anti-EU rhetoric. If Orban regains '
                    'momentum, axis reversal could halt or reverse.',
        'severity':       3,
        'color':          '#f97316',
        'icon':           '⚠️',
        'category':       'diplomatic_signal',
        'pressure_type':  'diplomatic',
        'source':         'Post-electoral defeat (April 2026), Fidesz retains '
                          '~33% of parliament + significant rural/Christian-'
                          'conservative base. Historical precedent: Orban returned '
                          'from his 2002-2010 opposition wilderness to win '
                          '2010 election decisively. Underestimate at peril.',
    },

    # ── Category C: EU NORMALIZATION (Diplomatic axis) ──────────
    {
        'id':       'eu_loan_unlock_active',
        'label':    'EU Loan / Funds Unlock Active',
        'detail':   '90B EUR Ukraine loan veto lifted + cohesion funds '
                    'released + Article 7 proceedings closing. Concrete '
                    'EU-Hungary normalization markers.',
        'severity':       1,
        'color':          '#22c55e',
        'icon':           '🇪🇺',
        'category':       'diplomatic_signal',
        'pressure_type':  'diplomatic',
        'source':         'Post-Tisza election: EU has signaled willingness '
                          'to release frozen funds + close Article 7 if Hungary '
                          'continues reform path. Loan veto lift documented.',
    },

    # ── Category D: ECONOMIC REVERSAL (Economic axis) ───────────
    {
        'id':       'druzhba_pipeline_dispute',
        'label':    'Druzhba Pipeline Status Dispute',
        'detail':   'Druzhba pipeline (Russia -> Ukraine -> Hungary -> '
                    'Slovakia) flow disrupted, damaged, or under repair. '
                    'Pre-election: Orban used Druzhba interruption as the '
                    'lever for EU loan veto. Post-election: flow resumption '
                    'allowed veto lift. Status is a structural pressure '
                    'indicator.',
        'severity':       2,
        'color':          '#f59e0b',
        'icon':           '🛢️',
        'category':       'economic_signal',
        'pressure_type':  'economic',
        'source':         'Reuters + AP reporting on Druzhba damage from '
                          'Russian drone strikes on Ukrainian territory, '
                          'subsequent repair + flow resumption.',
    },

    # ── Category E: GOODWILL EVENTS (Diplomatic axis) ───────────
    {
        'id':       'seized_assets_returned',
        'label':    'Hungary Returns Seized Ukrainian Assets',
        'detail':   'May 6 2026: Hungary returned $82M cash + 9kg gold '
                    'shipment seized March 5 2026 (between Oschadbank '
                    'transfers). Concrete goodwill marker between Tisza '
                    'government and Kyiv.',
        'severity':       1,
        'color':          '#22c55e',
        'icon':           '🤝',
        'category':       'diplomatic_signal',
        'pressure_type':  'diplomatic',
        'source':         'AP/Justin Spike May 6 2026 reporting. Asset return '
                          'reverses Orban-era seizure used as political tool. '
                          'Zelenskyy publicly thanked Hungary for "constructive '
                          'approach and civilized step."',
    },
]


# ============================================================
# GREEN LINES (positive diplomatic signals)
# ============================================================
GREEN_LINES = [
    {
        'id':     'tisza_eu_normalization',
        'label':  'Tisza-EU Normalization Track',
        'detail': 'Tisza government public commitments to EU rule-of-law '
                  'norms + cooperation. Article 7 proceedings progressing '
                  'toward closure.',
        'icon':   '✅',
        'weight': 1.2,
    },
    {
        'id':     'hungary_ukraine_warming',
        'label':  'Hungary-Ukraine Bilateral Warming',
        'detail': 'Returned assets + Zelensky-Magyar engagement + likely '
                  'shift on Ukraine EU accession veto.',
        'icon':   '🤝',
        'weight': 1.1,
    },
    {
        'id':     'paks_ii_review',
        'label':  'Paks II Rosatom Contract Under Review',
        'detail': 'New government reviewing the Rosatom-built nuclear plant '
                  'expansion contract -- structural Russia decoupling signal.',
        'icon':   '🔌',
        'weight': 1.0,
    },
    {
        'id':     'sanctions_compliance_increase',
        'label':  'Hungary Sanctions Compliance Increasing',
        'detail': 'Hungary now blocking fewer EU sanctions packages on Russia '
                  '-- structural reversal of obstruction pattern.',
        'icon':   '🛂',
        'weight': 1.0,
    },
]


# ============================================================
# HISTORICAL PRECEDENTS
# ============================================================
HISTORICAL_PRECEDENTS = [
    {
        'id':          'hungary_1989_transition',
        'label':       '1989 Hungarian Democratic Transition',
        'period':      'May-October 1989',
        'context':     ('Hungary pioneered Eastern Bloc democratic transition: '
                        'cut barbed wire on Austrian border (May 1989), opened '
                        'borders to East German refugees (September 1989), '
                        'declared republic (October 1989). First Warsaw Pact '
                        'country to fully exit Soviet orbit by domestic political '
                        'process rather than revolutionary rupture.'),
        'analog_for':  ['axis_reversal_in_progress', 'tisza_eu_normalization'],
        'icon':        '🕊️',
    },
    {
        'id':          'hungary_1956_revolution',
        'label':       '1956 Hungarian Revolution',
        'period':      'October-November 1956',
        'context':     ('Hungarian anti-Soviet uprising crushed by Soviet military '
                        'intervention; Imre Nagy executed. Cautionary precedent: '
                        'when an axis-dependent country attempts rapid reversal '
                        'AND has no security backstop, the patron power may '
                        'apply kinetic counter-pressure. Modern Hungary in NATO/EU '
                        'has structural backstop the 1956 government did not.'),
        'analog_for':  ['orban_revival_signal', 'druzhba_pipeline_dispute'],
        'icon':        '⚔️',
    },
    {
        'id':          'orban_2002_opposition_decade',
        'label':       'Orban 2002-2010 Opposition Wilderness',
        'period':      'May 2002 - April 2010',
        'context':     ('Orban lost the 2002 Hungarian election after his '
                        'first prime ministerial term, spent 8 years in '
                        'opposition, returned in 2010 with a two-thirds majority '
                        'and stayed in power 14 years. Demonstrates that Fidesz '
                        'is structurally durable as an opposition vehicle and '
                        'capable of long-cycle comebacks.'),
        'analog_for':  ['orban_revival_signal'],
        'icon':        '♻️',
    },
]


# ============================================================
# SCORING FUNCTIONS
# ============================================================
def _scan_articles_text(scan_data):
    """Build a single text blob from all articles + tripwires for keyword matching."""
    text = ''
    actors = scan_data.get('actors', {}) or {}
    for actor_data in actors.values():
        for art in (actor_data.get('top_articles', []) or []):
            text += ' ' + (art.get('title') or '').lower()
            text += ' ' + (art.get('description') or '').lower()
        for tw in (actor_data.get('tripwire_hits', []) or []):
            text += ' ' + str(tw).lower()
    return text


def _score_red_lines(scan_data):
    """
    Score each red line. Returns list of dicts with status field added.
    Status: BREACHED | APPROACHING | INACTIVE
    """
    cross_theater = scan_data.get('cross_theater', {}) or {}
    actors = scan_data.get('actors', {}) or {}
    text = _scan_articles_text(scan_data)

    triggered = []

    # 1. axis_reversal_in_progress -- BREACHED when 3+ reversal triggers fired
    reversal_active = cross_theater.get('axis_reversal_active', False)
    reversal_hits = cross_theater.get('axis_reversal_hits', []) or []
    if reversal_active or len(reversal_hits) >= 2:
        triggered.append({
            **next(r for r in RED_LINES if r['id'] == 'axis_reversal_in_progress'),
            'status':  'BREACHED' if reversal_active else 'APPROACHING',
            'trigger': (f'{len(reversal_hits)} axis-reversal triggers active: '
                        f'{", ".join(reversal_hits[:4])}'
                        if reversal_hits else 'Axis reversal pattern emerging'),
        })

    # 2. orban_revival_signal -- BREACHED when 2+ revival signals + Fidesz actor L3+
    revival_signal = cross_theater.get('orban_revival_signal', False)
    revival_hits = cross_theater.get('orban_revival_hits', []) or []
    opposition_level = (actors.get('hungary_opposition', {}) or {}).get('escalation_level', 0)
    if revival_signal or opposition_level >= 3:
        status = 'BREACHED' if (revival_signal and opposition_level >= 3) else 'APPROACHING'
        triggered.append({
            **next(r for r in RED_LINES if r['id'] == 'orban_revival_signal'),
            'status':  status,
            'trigger': (f'{len(revival_hits)} Orban-revival triggers + Fidesz at '
                        f'L{opposition_level}: {", ".join(revival_hits[:3])}'
                        if revival_hits else
                        f'Fidesz opposition at L{opposition_level} (TENSION-level)'),
        })

    # 3. eu_loan_unlock_active -- ACTIVE when loan/funds-related triggers fire
    loan_keywords = [
        'hungary lifts loan veto', 'hungary unlocks eu loan',
        'hungary eu funds released', 'hungary article 7 closed',
    ]
    loan_hits = [k for k in loan_keywords if k in text]
    if loan_hits:
        triggered.append({
            **next(r for r in RED_LINES if r['id'] == 'eu_loan_unlock_active'),
            'status':  'BREACHED' if len(loan_hits) >= 2 else 'APPROACHING',
            'trigger': f'EU loan/funds unlock signals active: {", ".join(loan_hits)}',
        })

    # 4. druzhba_pipeline_dispute -- ACTIVE when status disrupted/repairing
    druzhba_status = cross_theater.get('druzhba_pipeline_status', 'unknown')
    if druzhba_status in ('disrupted', 'repairing'):
        triggered.append({
            **next(r for r in RED_LINES if r['id'] == 'druzhba_pipeline_dispute'),
            'status':  'BREACHED' if druzhba_status == 'disrupted' else 'APPROACHING',
            'trigger': f'Druzhba pipeline status: {druzhba_status}',
        })

    # 5. seized_assets_returned -- BREACHED when return event detected
    asset_keywords = [
        'hungary returns ukraine assets', 'hungary returns gold ukraine',
        'hungary returns oschadbank', 'hungary returns 82 million',
        'hungary returns cash gold',
    ]
    asset_hits = [k for k in asset_keywords if k in text]
    if asset_hits:
        triggered.append({
            **next(r for r in RED_LINES if r['id'] == 'seized_assets_returned'),
            'status':  'BREACHED',
            'trigger': f'Seized-assets-return signal: {", ".join(asset_hits[:2])}',
        })

    return triggered


def _score_green_lines(scan_data):
    """Score positive diplomatic signals."""
    cross_theater = scan_data.get('cross_theater', {}) or {}
    actors = scan_data.get('actors', {}) or {}
    text = _scan_articles_text(scan_data)

    triggered = []

    # tisza_eu_normalization
    gov_level = (actors.get('hungary_government', {}) or {}).get('escalation_level', 0)
    eu_level  = (actors.get('hungary_eu_track', {}) or {}).get('escalation_level', 0)
    if gov_level >= 2 and eu_level >= 1:
        triggered.append({
            **next(g for g in GREEN_LINES if g['id'] == 'tisza_eu_normalization'),
            'status': 'ACTIVE',
            'trigger': f'Tisza gov L{gov_level} + EU track L{eu_level}',
        })

    # hungary_ukraine_warming
    ua_level = (actors.get('hungary_ukraine_track', {}) or {}).get('escalation_level', 0)
    if cross_theater.get('axis_reversal_active') or ua_level >= 2:
        triggered.append({
            **next(g for g in GREEN_LINES if g['id'] == 'hungary_ukraine_warming'),
            'status': 'ACTIVE',
            'trigger': f'Hungary-Ukraine track L{ua_level}; axis reversal active',
        })

    # paks_ii_review
    paks_keywords = ['paks ii review', 'paks ii rosatom review', 'paks ii contract review',
                     'rosatom hungary review', 'hungary nuclear contract review']
    if any(k in text for k in paks_keywords):
        triggered.append({
            **next(g for g in GREEN_LINES if g['id'] == 'paks_ii_review'),
            'status': 'ACTIVE',
            'trigger': 'Paks II Rosatom contract review signal detected',
        })

    # sanctions_compliance_increase
    if 'hungary unblocks sanctions' in text or 'hungary blocks fewer sanctions' in text:
        triggered.append({
            **next(g for g in GREEN_LINES if g['id'] == 'sanctions_compliance_increase'),
            'status': 'ACTIVE',
            'trigger': 'Hungary sanctions compliance increasing',
        })

    return triggered


def _score_diplomatic_track(scan_data, green_lines_triggered):
    """
    Compute the Hungary diplomatic-track score.

    Hungary's diplomatic track is the PRIMARY analytical axis for this country
    (unlike Russia where it's secondary to kinetic posture). Score reflects:
      - active green lines = positive diplomatic momentum
      - axis_reversal_active = strong positive
      - orban_revival_signal = negative drag
      - article-volume in EU/Ukraine tracks = engagement intensity
    """
    cross_theater = scan_data.get('cross_theater', {}) or {}
    actors = scan_data.get('actors', {}) or {}

    score = 0

    # Active green lines contribute positively
    for g in green_lines_triggered:
        if g.get('status') == 'ACTIVE':
            score += int(g.get('weight', 1.0) * 15)

    # Axis reversal active is a major positive
    if cross_theater.get('axis_reversal_active'):
        score += 25

    # Orban revival is a negative drag
    if cross_theater.get('orban_revival_signal'):
        score -= 20

    # EU + Ukraine engagement (article volume) adds to score
    eu_level  = (actors.get('hungary_eu_track', {}) or {}).get('escalation_level', 0)
    ua_level  = (actors.get('hungary_ukraine_track', {}) or {}).get('escalation_level', 0)
    score += (eu_level + ua_level) * 5

    # Cap 0-100
    score = max(0, min(100, score))

    # Map to scenario
    if score >= 75:
        scenario = 'STRONG NORMALIZATION -- axis reversal durable, EU integration accelerating'
        scenario_color = '#22c55e'
        scenario_icon  = '🟢'
    elif score >= 50:
        scenario = 'ACTIVE NORMALIZATION -- axis reversal in progress with positive momentum'
        scenario_color = '#3b82f6'
        scenario_icon  = '🔵'
    elif score >= 30:
        scenario = 'TENTATIVE NORMALIZATION -- reversal signals present but contested'
        scenario_color = '#f59e0b'
        scenario_icon  = '🟡'
    elif score >= 15:
        scenario = 'CONTESTED -- reversal signals offset by Orban-revival pressure'
        scenario_color = '#f97316'
        scenario_icon  = '🟠'
    else:
        scenario = 'STAGNANT or REVERSING -- axis reversal stalled or rolling back'
        scenario_color = '#dc2626'
        scenario_icon  = '🔴'

    # Maximum pressure flag (Orban revival dominant)
    max_pressure = (cross_theater.get('orban_revival_signal', False) and score < 30)

    return {
        'score':            score,
        'scenario':         scenario,
        'scenario_color':   scenario_color,
        'scenario_icon':    scenario_icon,
        'maximum_pressure': max_pressure,
    }


def _match_historical(scan_data):
    """Match scan against historical precedents."""
    cross_theater = scan_data.get('cross_theater', {}) or {}
    text = _scan_articles_text(scan_data)
    triggered_ids = scan_data.get('_triggered_red_line_ids', []) or []

    matches = []
    for precedent in HISTORICAL_PRECEDENTS:
        relevance_score = 0
        for analog in precedent.get('analog_for', []):
            if analog in triggered_ids:
                relevance_score += 1
        # Also check if precedent label keywords appear in text
        label_kw = precedent['label'].lower().split()[:3]
        if any(kw in text for kw in label_kw):
            relevance_score += 1
        if relevance_score > 0:
            matches.append({
                **precedent,
                'relevance_score': relevance_score,
            })

    matches.sort(key=lambda m: -m['relevance_score'])
    return matches[:3]


def _build_so_what(scan_data, red_lines_triggered, historical_matches,
                   green_lines_triggered, diplomatic):
    """
    Build the so-what scenario summary.
    """
    cross_theater = scan_data.get('cross_theater', {}) or {}

    breached    = [r for r in red_lines_triggered if r.get('status') == 'BREACHED']
    approaching = [r for r in red_lines_triggered if r.get('status') == 'APPROACHING']
    active_gl   = [g for g in green_lines_triggered if g.get('status') == 'ACTIVE']

    reversal_active = cross_theater.get('axis_reversal_active', False)
    revival_signal  = cross_theater.get('orban_revival_signal', False)

    # Build scenario selection logic
    if reversal_active and not revival_signal:
        scenario = 'AXIS REVERSAL CONSOLIDATING'
        scenario_color = '#22c55e'
        scenario_icon  = '🪜'
        situation = (
            'Hungary axis reversal is consolidating: returned seized Ukrainian assets, '
            'lifted EU loan veto, Druzhba flows resumed, Tisza government public '
            'commitments to EU norms. Orban/Fidesz NOT yet showing visible revival '
            'signals in this scan window.'
        )
        assessment = (
            'Hungary appears to be settling into post-Orban diplomatic posture. '
            'Window for EU funds release + Article 7 closure is open. Watch for: '
            '(a) Russia counter-pressure (gas pricing, Paks II financing leverage), '
            '(b) Fidesz organizational consolidation as opposition vehicle, '
            '(c) sustained EU-Hungary normalization signals over next 3-6 months.'
        )
        watch_list = [
            'Paks II Rosatom contract review outcome',
            'EU cohesion funds release timing',
            'Hungary lifting Ukraine EU accession veto',
            'Russian gas contract (MVM-Gazprom) renegotiation',
            'Orban international travel + summits',
        ]
    elif reversal_active and revival_signal:
        scenario = 'CONTESTED REVERSAL'
        scenario_color = '#f59e0b'
        scenario_icon  = '⚖️'
        situation = (
            'Hungary axis reversal underway BUT Orban/Fidesz showing visible '
            'revival signals (Moscow visits, mass rallies, Trump alignment, '
            'Tucker Carlson interviews). Tisza government continuing reversal '
            'measures while opposition organizes counter-pressure.'
        )
        assessment = (
            'High-friction phase. Outcome NOT predetermined. Two-thirds Tisza '
            'majority provides parliamentary insulation, but Fidesz can apply '
            'pressure via street politics, international ties, and rural base. '
            'Russia + Trump alignment with Orban is the asymmetric leverage.'
        )
        watch_list = [
            'Orban-Putin meetings + statements',
            'Orban-Trump direct channel signals',
            'Fidesz rally attendance + frequency',
            'Tisza government polling stability',
            'Russia counter-pressure on Hungarian energy',
        ]
    elif revival_signal and not reversal_active:
        scenario = 'ORBAN COMEBACK FORMING'
        scenario_color = '#f97316'
        scenario_icon  = '⚠️'
        situation = (
            'Limited axis-reversal signals observed AND Orban/Fidesz revival '
            'signals present. Either Tisza government is moving too slowly on '
            'reversal commitments OR scan window is missing key signals OR '
            'opposition is dominating the rhetorical space.'
        )
        assessment = (
            'Concerning trajectory. Historical precedent (Orban 2002-2010) shows '
            'Fidesz can build comeback over multi-year cycles. If Tisza government '
            'fails to deliver visible EU normalization + economic dividends, '
            'Orban-Fidesz could win next election.'
        )
        watch_list = [
            'Tisza government legislative outputs (visible reforms)',
            'EU funds disbursement to Hungary (visible benefit)',
            'Fidesz polling trajectory',
            'Russia/Trump pressure operations on Hungarian economy',
            'Tisza coalition stability',
        ]
    else:
        scenario = 'BASELINE -- LIMITED SIGNAL'
        scenario_color = '#6b7280'
        scenario_icon  = '⚪'
        situation = (
            'Scan window shows limited Hungary diplomatic signal flow. May reflect '
            'a slow news week, scan-source gaps, or genuine baseline (the months '
            'after a landslide election often have a quieter signal period as '
            'new government organizes).'
        )
        assessment = (
            'No immediate red flags. Continue monitoring. Hungary tracker is '
            'now active and will surface signals as they emerge.'
        )
        watch_list = [
            'Tisza cabinet appointments + first policy announcements',
            'EU response to Hungarian normalization',
            'Russia statements on Hungary',
            'Druzhba pipeline operational status',
            'Hungarian opposition organizational moves',
        ]

    return {
        'scenario':       scenario,
        'scenario_color': scenario_color,
        'scenario_icon':  scenario_icon,
        'situation':      situation,
        'assessment':     assessment,
        'watch_list':     watch_list,
        'breached_count':    len(breached),
        'approaching_count': len(approaching),
        'green_lines_active': len(active_gl),
    }


def _inject_triggered_ids(scan_data, red_lines_triggered):
    """Inject triggered red line IDs so _match_historical can detect patterns."""
    if not isinstance(scan_data, dict):
        return scan_data
    scan_data['_triggered_red_line_ids'] = [r.get('id') for r in red_lines_triggered]
    return scan_data


# ============================================================
# MAIN INTERPRETER ENTRY POINT
# ============================================================
def interpret_signals(scan_data):
    """
    Main entry point. Called from rhetoric_tracker_hungary.py.
    Returns interpretation dict mirroring the Russia interpreter contract.
    """
    try:
        red_lines   = _score_red_lines(scan_data)
        green_lines = _score_green_lines(scan_data)
        diplomatic  = _score_diplomatic_track(scan_data, green_lines)
        scan_data   = _inject_triggered_ids(scan_data, red_lines)
        historical  = _match_historical(scan_data)
        so_what     = _build_so_what(scan_data, red_lines, historical,
                                     green_lines, diplomatic)

        breached    = [r for r in red_lines if r.get('status') == 'BREACHED']
        approaching = [r for r in red_lines if r.get('status') == 'APPROACHING']
        active_gl   = [g for g in green_lines if g.get('status') == 'ACTIVE']

        return {
            'so_what':             so_what,
            'red_lines': {
                'triggered':         red_lines,
                'breached_count':    len(breached),
                'approaching_count': len(approaching),
                'highest_severity':  max((r.get('severity', 0) for r in red_lines), default=0),
            },
            'green_lines': {
                'triggered':         green_lines,
                'active_count':      len(active_gl),
                'signaled_count':    len(green_lines) - len(active_gl),
                'diplomatic_score':  diplomatic['score'],
            },
            'diplomatic_track':    diplomatic,
            'historical_matches':  historical,
            'interpreter_version': '1.0.0',
            'interpreted_at':      datetime.now(timezone.utc).isoformat(),
        }
    except Exception as e:
        print(f'[Hungary Interpreter] Error: {str(e)[:120]}')
        return {
            'so_what': {
                'scenario': 'Interpreter error',
                'assessment': str(e)[:200],
                'situation': '',
                'watch_list': [],
                'scenario_color': '#6b7280',
                'scenario_icon': '⚪',
            },
            'red_lines': {
                'triggered': [],
                'breached_count': 0,
                'approaching_count': 0,
                'highest_severity': 0,
            },
            'green_lines': {
                'triggered': [],
                'active_count': 0,
                'signaled_count': 0,
                'diplomatic_score': 0,
            },
            'diplomatic_track': {
                'score': 0,
                'scenario': 'Unknown',
                'maximum_pressure': False,
                'scenario_color': '#6b7280',
                'scenario_icon': '⚪',
            },
            'historical_matches': [],
            'interpreter_version': '1.0.0',
            'error': str(e)[:200],
        }


# ============================================================
# MODULE METADATA
# ============================================================
__version__ = '1.0.0'
__module_id__ = 'hungary_signal_interpreter'
print(f'[Hungary Interpreter] Module loaded -- v{__version__}')
