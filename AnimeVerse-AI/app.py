import { useState } from "react";

const JIKAN_BASE = "https://api.jikan.moe/v4";

const CHARACTER_IMAGES = {
  "Naruto Uzumaki": "https://cdn.myanimelist.net/images/characters/2/284121.jpg",
  "Monkey D. Luffy": "https://cdn.myanimelist.net/images/characters/9/310307.jpg",
  "Itachi Uchiha": "https://cdn.myanimelist.net/images/characters/11/131115.jpg",
  "Levi Ackerman": "https://cdn.myanimelist.net/images/characters/2/241413.jpg",
  "Gojo Satoru": "https://cdn.myanimelist.net/images/characters/9/422188.jpg",
  "Goku": "https://cdn.myanimelist.net/images/characters/10/396411.jpg",
  "Eren Yeager": "https://cdn.myanimelist.net/images/characters/10/216895.jpg",
  "Saitama": "https://cdn.myanimelist.net/images/characters/13/284121.jpg",
};

const CHARACTER_DESCRIPTIONS = {
  "Naruto Uzumaki": "You never give up, no matter how hard things get. You fight for your friends and carry the weight of the world with a smile.",
  "Monkey D. Luffy": "You live for freedom and adventure. You're fiercely loyal to your crew and charge headfirst into any challenge.",
  "Itachi Uchiha": "You're calm, calculated, and deeply strategic. You make hard sacrifices and carry your burdens in silence.",
  "Levi Ackerman": "You're disciplined, precise, and efficient. You adapt quickly and hold yourself to an impossibly high standard.",
  "Gojo Satoru": "You're brilliantly talented and a little overconfident. You protect others with a laugh but never underestimate a threat.",
  "Goku": "You live to grow stronger. Battle is your joy and your purpose, and you never stop pushing your limits.",
  "Eren Yeager": "You're driven by an unyielding vision of freedom. Your conviction is absolute — even if others don't understand it yet.",
  "Saitama": "You're unmatched in raw power but searching for real challenge and meaning. You keep going, one punch at a time.",
};

const QUOTES = {
  Motivational: [
    { char: "Naruto Uzumaki", quote: "I'm not gonna run away, I never go back on my word! That's my nindo, my ninja way!" },
    { char: "Rock Lee", quote: "A dropout will beat a genius through hard work." },
    { char: "All Might", quote: "It's fine now. Why? Because I am here!" },
    { char: "Goku", quote: "Power comes in response to a need, not a desire." },
  ],
  Friendship: [
    { char: "Monkey D. Luffy", quote: "I don't want to conquer anything. I just think the guy with the most freedom in the world is the Pirate King." },
    { char: "Naruto Uzumaki", quote: "I won't let my comrades die. I'll protect everyone." },
    { char: "Edward Elric", quote: "A lesson without pain is meaningless. You can't gain something without giving something in return." },
  ],
  Success: [
    { char: "Itachi Uchiha", quote: "Reality is often cruel and unjust. That is why humans can change the world." },
    { char: "Light Yagami", quote: "I am justice! I protect the innocent and pass judgment on the wicked." },
    { char: "Kakashi Hatake", quote: "Those who break the rules are scum, but those who abandon their friends are worse than scum." },
  ],
  Sad: [
    { char: "Pain", quote: "Even if it means sacrificing my own life, I have to do what I have to do." },
    { char: "Itachi Uchiha", quote: "Forgive me, Sasuke. It ends with this." },
    { char: "Guts", quote: "Even if we painstakingly piece together something lost, it doesn't mean things will ever go back to how they were." },
  ],
  Funny: [
    { char: "Saitama", quote: "Ok." },
    { char: "Goku", quote: "I am the hope of the universe. I am the answer to all living things that cry out for peace." },
    { char: "Korosensei", quote: "A mediocre teacher tells. A good teacher explains. A great teacher demonstrates. An excellent teacher inspires." },
  ],
};

function getCharacterMatch(answers) {
  const score = {
    "Naruto Uzumaki": 0, "Monkey D. Luffy": 0, "Itachi Uchiha": 0,
    "Levi Ackerman": 0, "Gojo Satoru": 0, "Goku": 0,
    "Eren Yeager": 0, "Saitama": 0,
  };
  for (const a of answers) {
    if (["Friendship", "Support", "Loyalty"].includes(a)) {
      score["Naruto Uzumaki"] += 2; score["Monkey D. Luffy"] += 2;
      score["Itachi Uchiha"] += 2; score["Saitama"] += 1;
    }
    if (a === "Freedom") { score["Monkey D. Luffy"] += 3; score["Eren Yeager"] += 2; }
    if (["Power", "Physical strength"].includes(a)) {
      score["Goku"] += 3; score["Saitama"] += 2; score["Gojo Satoru"] += 2;
      score["Naruto Uzumaki"] += 1; score["Itachi Uchiha"] += 1;
    }
    if (["Strategic", "Intelligence", "Tactical mind"].includes(a)) {
      score["Itachi Uchiha"] += 3; score["Levi Ackerman"] += 3; score["Gojo Satoru"] += 1;
    }
    if (a === "Knowledge") { score["Itachi Uchiha"] += 2; score["Levi Ackerman"] += 1; }
    if (a === "Courage") {
      score["Naruto Uzumaki"] += 2; score["Monkey D. Luffy"] += 3; score["Goku"] += 2;
    }
    if (["Anger", "Overconfidence"].includes(a)) { score["Eren Yeager"] += 3; score["Gojo Satoru"] += 1; }
    if (["Trust issues"].includes(a)) { score["Itachi Uchiha"] += 2; score["Levi Ackerman"] += 1; }
    if (a === "Fear") { score["Naruto Uzumaki"] += 1; score["Eren Yeager"] += 1; }
    if (a === "Calmness") { score["Itachi Uchiha"] += 2; score["Gojo Satoru"] += 2; }
    if (a === "Speed") {
      score["Goku"] += 2; score["Naruto Uzumaki"] += 1; score["Levi Ackerman"] += 2;
    }
    if (["Magic/Skills"].includes(a)) { score["Gojo Satoru"] += 3; score["Naruto Uzumaki"] += 1; }
    if (a === "Leader") {
      score["Naruto Uzumaki"] += 2; score["Eren Yeager"] += 2; score["Monkey D. Luffy"] += 2;
    }
    if (a === "Lone wolf") { score["Itachi Uchiha"] += 2; score["Levi Ackerman"] += 2; score["Goku"] += 1; }
    if (a === "Strategist") { score["Itachi Uchiha"] += 2; score["Levi Ackerman"] += 2; }
    if (["Head on"].includes(a)) { score["Goku"] += 2; score["Naruto Uzumaki"] += 2; score["Monkey D. Luffy"] += 2; }
    if (a === "Adapt") {
      score["Levi Ackerman"] += 2; score["Goku"] += 2;
      score["Itachi Uchiha"] += 3; score["Saitama"] += 1;
    }
  }
  const total = Object.values(score).reduce((a, b) => a + b, 0);
  const percentages = {};
  for (const [k, v] of Object.entries(score)) percentages[k] = Math.round((v / (total || 1)) * 100);
  const winner = Object.keys(score).reduce((a, b) => score[a] > score[b] ? a : b);
  return { winner, percentages };
}

const BATTLE_CHARS = ["Naruto Uzumaki", "Monkey D. Luffy", "Goku", "Saitama", "Itachi Uchiha", "Levi Ackerman", "Gojo Satoru", "Eren Yeager", "Ichigo Kurosaki", "Madara Uchiha", "Whitebeard", "Aizen", "Meliodas", "Rimuru Tempest"];

const CHAR_STATS = {
  "Naruto Uzumaki": { power: 97, speed: 95, defense: 88, intelligence: 82 },
  "Monkey D. Luffy": { power: 96, speed: 92, defense: 85, intelligence: 75 },
  "Goku": { power: 100, speed: 99, defense: 92, intelligence: 72 },
  "Saitama": { power: 100, speed: 100, defense: 100, intelligence: 65 },
  "Itachi Uchiha": { power: 92, speed: 91, defense: 80, intelligence: 99 },
  "Levi Ackerman": { power: 88, speed: 97, defense: 78, intelligence: 90 },
  "Gojo Satoru": { power: 98, speed: 96, defense: 95, intelligence: 95 },
  "Eren Yeager": { power: 94, speed: 86, defense: 90, intelligence: 78 },
  "Ichigo Kurosaki": { power: 95, speed: 94, defense: 88, intelligence: 80 },
  "Madara Uchiha": { power: 99, speed: 93, defense: 96, intelligence: 97 },
  "Whitebeard": { power: 98, speed: 80, defense: 97, intelligence: 88 },
  "Aizen": { power: 97, speed: 95, defense: 93, intelligence: 100 },
  "Meliodas": { power: 96, speed: 95, defense: 90, intelligence: 82 },
  "Rimuru Tempest": { power: 98, speed: 97, defense: 99, intelligence: 96 },
};

function getStats(name) {
  return CHAR_STATS[name] || {
    power: 70 + Math.floor(Math.random() * 30),
    speed: 70 + Math.floor(Math.random() * 30),
    defense: 70 + Math.floor(Math.random() * 30),
    intelligence: 70 + Math.floor(Math.random() * 30),
  };
}

function calcScore(stats) {
  return stats.power * 0.35 + stats.speed * 0.25 + stats.defense * 0.2 + stats.intelligence * 0.2 + Math.random() * 10;
}

function battle1v1(a, b) {
  const sa = calcScore(getStats(a)), sb = calcScore(getStats(b));
  const winner = sa >= sb ? a : b;
  const margin = Math.abs(sa - sb);
  const closeness = margin < 5 ? "an incredibly close fight" : margin < 15 ? "a hard-fought battle" : "a decisive victory";
  const finishers = ["Rasengan!", "Gear Fifth!", "Kamehameha!", "Infinity!", "Hakai!", "Omniscience:", "Titan roar!", "Flash Step!"];
  const finisher = finishers[Math.floor(Math.random() * finishers.length)];
  return { winner, loser: winner === a ? b : a, log: [`${a} vs ${b} ${closeness}!`, `${winner} lands the finishing blow: ${finisher}`, `Winner: ${winner}`] };
}

function battleTeam(teamA, teamB) {
  const scoreA = teamA.reduce((s, c) => s + calcScore(getStats(c)), 0);
  const scoreB = teamB.reduce((s, c) => s + calcScore(getStats(c)), 0);
  return { winner: scoreA >= scoreB ? teamA : teamB, loser: scoreA >= scoreB ? teamB : teamA };
}

function runTournament(chars) {
  let pool = [...chars];
  const rounds = [];
  while (pool.length > 1) {
    const roundResults = [];
    const nextPool = [];
    for (let i = 0; i < pool.length - 1; i += 2) {
      const r = battle1v1(pool[i], pool[i + 1]);
      roundResults.push(r);
      nextPool.push(r.winner);
    }
    if (pool.length % 2 !== 0) nextPool.push(pool[pool.length - 1]);
    rounds.push(roundResults);
    pool = nextPool;
  }
  return { rounds, champion: pool[0] };
}

function survivalMode(chars) {
  let current = chars[0];
  const log = [];
  for (let i = 1; i < chars.length; i++) {
    const r = battle1v1(current, chars[i]);
    log.push({ fight: `${current} vs ${chars[i]}`, winner: r.winner });
    current = r.winner;
  }
  return { survivor: current, log };
}

const TABS = ["Search", "Battle", "Quotes", "Quiz", "Login"];
const TAB_ICONS = ["ti-search", "ti-sword", "ti-message-2", "ti-user-question", "ti-lock"];

export default function App() {
  const [activeTab, setActiveTab] = useState(0);
  const [users, setUsers] = useState({});
  const [loggedIn, setLoggedIn] = useState(null);

  return (
    <div style={{ fontFamily: "var(--font-sans)", color: "var(--color-text-primary)", padding: "0 0 2rem" }}>
      <header style={{ borderBottom: "0.5px solid var(--color-border-tertiary)", padding: "1rem 1.25rem 0", marginBottom: "1.5rem" }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: "1rem" }}>
          <div>
            <h1 style={{ margin: 0, fontSize: 22, fontWeight: 500 }}>AnimeVerse AI</h1>
            <p style={{ margin: 0, fontSize: 13, color: "var(--color-text-secondary)" }}>
              {loggedIn ? `Welcome back, ${loggedIn}` : "AI-powered anime companion"}
            </p>
          </div>
          {loggedIn && (
            <button onClick={() => setLoggedIn(null)} style={{ fontSize: 13, color: "var(--color-text-secondary)", background: "none", border: "0.5px solid var(--color-border-secondary)", borderRadius: "var(--border-radius-md)", padding: "4px 12px", cursor: "pointer" }}>
              Sign out
            </button>
          )}
        </div>
        <nav style={{ display: "flex", gap: 4 }}>
          {TABS.map((tab, i) => (
            <button key={tab} onClick={() => setActiveTab(i)} style={{
              background: activeTab === i ? "var(--color-background-secondary)" : "none",
              border: "none", borderBottom: activeTab === i ? "2px solid var(--color-text-primary)" : "2px solid transparent",
              padding: "8px 14px", fontSize: 14, cursor: "pointer",
              color: activeTab === i ? "var(--color-text-primary)" : "var(--color-text-secondary)",
              borderRadius: "var(--border-radius-md) var(--border-radius-md) 0 0",
              display: "flex", alignItems: "center", gap: 6,
            }}>
              <i className={`ti ${TAB_ICONS[i]}`} style={{ fontSize: 15 }} aria-hidden="true" />
              {tab}
            </button>
          ))}
        </nav>
      </header>

      <div style={{ padding: "0 1.25rem" }}>
        {activeTab === 0 && <SearchTab />}
        {activeTab === 1 && <BattleTab />}
        {activeTab === 2 && <QuotesTab />}
        {activeTab === 3 && <QuizTab />}
        {activeTab === 4 && <LoginTab users={users} setUsers={setUsers} loggedIn={loggedIn} setLoggedIn={setLoggedIn} />}
      </div>
    </div>
  );
}

function SearchTab() {
  const [query, setQuery] = useState("");
  const [anime, setAnime] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function searchAnime() {
    if (!query.trim()) return;
    setLoading(true); setError(""); setAnime(null);
    try {
      const res = await fetch(`${JIKAN_BASE}/anime?q=${encodeURIComponent(query)}&limit=1`);
      if (!res.ok) throw new Error("API request failed");
      const data = await res.json();
      if (!data.data || data.data.length === 0) { setError("No anime found. Try a different name."); }
      else setAnime(data.data[0]);
    } catch (e) {
      setError(e.message || "Something went wrong. Check your connection.");
    } finally { setLoading(false); }
  }

  return (
    <div>
      <h2 style={{ fontSize: 18, fontWeight: 500, marginBottom: "1rem" }}>Anime search</h2>
      <div style={{ display: "flex", gap: 8, marginBottom: "1.5rem" }}>
        <input value={query} onChange={e => setQuery(e.target.value)}
          onKeyDown={e => e.key === "Enter" && searchAnime()}
          placeholder="Enter anime name…" style={{ flex: 1 }} />
        <button onClick={searchAnime} disabled={loading} style={{ padding: "0 20px" }}>
          {loading ? "Searching…" : "Search"}
        </button>
      </div>

      {error && <p style={{ color: "var(--color-text-danger)", fontSize: 14 }}>{error}</p>}

      {anime && (
        <div style={{ display: "flex", gap: "1.5rem", flexWrap: "wrap" }}>
          <img src={anime.images?.jpg?.image_url} alt={anime.title} style={{ width: 180, borderRadius: "var(--border-radius-lg)", border: "0.5px solid var(--color-border-tertiary)", objectFit: "cover" }} />
          <div style={{ flex: 1, minWidth: 200 }}>
            <h3 style={{ margin: "0 0 4px", fontSize: 20, fontWeight: 500 }}>{anime.title}</h3>
            {anime.title_english && anime.title_english !== anime.title && (
              <p style={{ margin: "0 0 12px", fontSize: 13, color: "var(--color-text-secondary)" }}>{anime.title_english}</p>
            )}
            <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 12 }}>
              <Pill icon="ti-star" label={anime.score ? `${anime.score}/10` : "N/A"} />
              <Pill icon="ti-device-tv" label={anime.episodes ? `${anime.episodes} eps` : "Unknown eps"} />
              <Pill icon="ti-calendar" label={anime.year || "Year unknown"} />
              {anime.status && <Pill icon="ti-circle-check" label={anime.status} />}
            </div>
            {anime.genres?.length > 0 && (
              <p style={{ fontSize: 13, color: "var(--color-text-secondary)", margin: "0 0 12px" }}>
                <strong style={{ fontWeight: 500, color: "var(--color-text-primary)" }}>Genres: </strong>
                {anime.genres.map(g => g.name).join(", ")}
              </p>
            )}
            {anime.synopsis && (
              <p style={{ fontSize: 13, color: "var(--color-text-secondary)", lineHeight: 1.6, margin: 0, display: "-webkit-box", WebkitLineClamp: 5, WebkitBoxOrient: "vertical", overflow: "hidden" }}>
                {anime.synopsis}
              </p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

function Pill({ icon, label }) {
  return (
    <span style={{ display: "inline-flex", alignItems: "center", gap: 4, fontSize: 13, padding: "3px 10px", borderRadius: 999, background: "var(--color-background-secondary)", border: "0.5px solid var(--color-border-tertiary)", color: "var(--color-text-secondary)" }}>
      <i className={`ti ${icon}`} style={{ fontSize: 13 }} aria-hidden="true" />
      {label}
    </span>
  );
}

function BattleTab() {
  const [mode, setMode] = useState("1v1");
  const [inputs, setInputs] = useState({ a: "", b: "", a2: "", b2: "", teamA: ["", "", "", ""], teamB: ["", "", "", ""], tournamentChars: Array(8).fill(""), survivalChars: Array(6).fill("") });
  const [result, setResult] = useState(null);
  const [animating, setAnimating] = useState(false);

  function setIn(key, val) { setInputs(p => ({ ...p, [key]: val })); }
  function setTeam(team, idx, val) {
    setInputs(p => {
      const arr = [...p[team]]; arr[idx] = val; return { ...p, [team]: arr };
    });
  }

  function runBattle() {
    setAnimating(true); setResult(null);
    setTimeout(() => {
      let res;
      if (mode === "1v1") res = { type: "1v1", ...battle1v1(inputs.a || "Character A", inputs.b || "Character B") };
      else if (mode === "2v2") {
        const tA = [inputs.a || "Fighter A1", inputs.a2 || "Fighter A2"];
        const tB = [inputs.b || "Fighter B1", inputs.b2 || "Fighter B2"];
        const r = battleTeam(tA, tB);
        res = { type: "2v2", winner: r.winner.join(" & "), loser: r.loser.join(" & ") };
      } else if (mode === "4v4") {
        const tA = inputs.teamA.map((c, i) => c || `Team A Fighter ${i + 1}`);
        const tB = inputs.teamB.map((c, i) => c || `Team B Fighter ${i + 1}`);
        const r = battleTeam(tA, tB);
        res = { type: "4v4", winner: r.winner.join(", "), loser: r.loser.join(", ") };
      } else if (mode === "tournament") {
        const chars = inputs.tournamentChars.map((c, i) => c || `Fighter ${i + 1}`);
        res = { type: "tournament", ...runTournament(chars) };
      } else if (mode === "survival") {
        const chars = inputs.survivalChars.map((c, i) => c || `Fighter ${i + 1}`);
        res = { type: "survival", ...survivalMode(chars) };
      }
      setResult(res); setAnimating(false);
    }, 900);
  }

  const CHAR_OPTS = BATTLE_CHARS.map(c => <option key={c} value={c}>{c}</option>);

  return (
    <div>
      <h2 style={{ fontSize: 18, fontWeight: 500, marginBottom: "1rem" }}>Battle simulator</h2>
      <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: "1.5rem" }}>
        {[["1v1", "1v1"], ["2v2", "2v2"], ["4v4", "4v4"], ["tournament", "Tournament"], ["survival", "Survival"]].map(([val, label]) => (
          <button key={val} onClick={() => { setMode(val); setResult(null); }} style={{ background: mode === val ? "var(--color-background-secondary)" : "none", borderColor: mode === val ? "var(--color-border-primary)" : "var(--color-border-secondary)", fontWeight: mode === val ? 500 : 400 }}>
            {label}
          </button>
        ))}
      </div>

      {mode === "1v1" && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr auto 1fr", alignItems: "center", gap: 12, marginBottom: 16 }}>
          <select value={inputs.a} onChange={e => setIn("a", e.target.value)} style={{ width: "100%" }}><option value="">Fighter A</option>{CHAR_OPTS}</select>
          <span style={{ fontSize: 14, color: "var(--color-text-secondary)", fontWeight: 500 }}>vs</span>
          <select value={inputs.b} onChange={e => setIn("b", e.target.value)} style={{ width: "100%" }}><option value="">Fighter B</option>{CHAR_OPTS}</select>
        </div>
      )}

      {mode === "2v2" && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr auto 1fr", gap: 12, marginBottom: 16 }}>
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            <select value={inputs.a} onChange={e => setIn("a", e.target.value)}><option value="">Team A — Fighter 1</option>{CHAR_OPTS}</select>
            <select value={inputs.a2} onChange={e => setIn("a2", e.target.value)}><option value="">Team A — Fighter 2</option>{CHAR_OPTS}</select>
          </div>
          <span style={{ fontSize: 14, color: "var(--color-text-secondary)", fontWeight: 500, alignSelf: "center" }}>vs</span>
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            <select value={inputs.b} onChange={e => setIn("b", e.target.value)}><option value="">Team B — Fighter 1</option>{CHAR_OPTS}</select>
            <select value={inputs.b2} onChange={e => setIn("b2", e.target.value)}><option value="">Team B — Fighter 2</option>{CHAR_OPTS}</select>
          </div>
        </div>
      )}

      {mode === "4v4" && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr auto 1fr", gap: 12, marginBottom: 16 }}>
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {inputs.teamA.map((c, i) => (
              <select key={i} value={c} onChange={e => setTeam("teamA", i, e.target.value)}>
                <option value="">Team A — Fighter {i + 1}</option>{CHAR_OPTS}
              </select>
            ))}
          </div>
          <span style={{ fontSize: 14, color: "var(--color-text-secondary)", fontWeight: 500, alignSelf: "center" }}>vs</span>
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {inputs.teamB.map((c, i) => (
              <select key={i} value={c} onChange={e => setTeam("teamB", i, e.target.value)}>
                <option value="">Team B — Fighter {i + 1}</option>{CHAR_OPTS}
              </select>
            ))}
          </div>
        </div>
      )}

      {mode === "tournament" && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, marginBottom: 16 }}>
          {inputs.tournamentChars.map((c, i) => (
            <select key={i} value={c} onChange={e => setTeam("tournamentChars", i, e.target.value)}>
              <option value="">Participant {i + 1}</option>{CHAR_OPTS}
            </select>
          ))}
        </div>
      )}

      {mode === "survival" && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, marginBottom: 16 }}>
          {inputs.survivalChars.map((c, i) => (
            <select key={i} value={c} onChange={e => setTeam("survivalChars", i, e.target.value)}>
              <option value="">Arena Fighter {i + 1}</option>{CHAR_OPTS}
            </select>
          ))}
        </div>
      )}

      <button onClick={runBattle} disabled={animating} style={{ padding: "8px 24px", fontWeight: 500 }}>
        {animating ? "⚔️ Fighting…" : "⚔️ Start battle"}
      </button>

      {result && !animating && (
        <div style={{ marginTop: "1.5rem" }}>
          {(result.type === "1v1" || result.type === "2v2" || result.type === "4v4") && (
            <div style={{ background: "var(--color-background-secondary)", borderRadius: "var(--border-radius-lg)", padding: "1.25rem", border: "0.5px solid var(--color-border-tertiary)" }}>
              <p style={{ margin: "0 0 8px", fontSize: 13, color: "var(--color-text-secondary)" }}>Battle result</p>
              <p style={{ margin: "0 0 4px", fontSize: 20, fontWeight: 500 }}>🏆 {result.winner}</p>
              <p style={{ margin: 0, fontSize: 14, color: "var(--color-text-secondary)" }}>defeated {result.loser}</p>
              {result.log && (
                <div style={{ marginTop: 12, borderTop: "0.5px solid var(--color-border-tertiary)", paddingTop: 12 }}>
                  {result.log.map((l, i) => <p key={i} style={{ margin: "2px 0", fontSize: 13, color: i === result.log.length - 1 ? "var(--color-text-primary)" : "var(--color-text-secondary)" }}>{l}</p>)}
                </div>
              )}
            </div>
          )}

          {result.type === "tournament" && (
            <div style={{ background: "var(--color-background-secondary)", borderRadius: "var(--border-radius-lg)", padding: "1.25rem", border: "0.5px solid var(--color-border-tertiary)" }}>
              <p style={{ margin: "0 0 8px", fontSize: 13, color: "var(--color-text-secondary)" }}>Tournament results</p>
              <p style={{ margin: "0 0 16px", fontSize: 20, fontWeight: 500 }}>🏆 Champion: {result.champion}</p>
              {result.rounds.map((round, ri) => (
                <div key={ri} style={{ marginBottom: 12 }}>
                  <p style={{ margin: "0 0 6px", fontSize: 13, fontWeight: 500 }}>Round {ri + 1}</p>
                  {round.map((r, i) => (
                    <p key={i} style={{ margin: "2px 0", fontSize: 13, color: "var(--color-text-secondary)" }}>
                      {r.winner} <span style={{ color: "var(--color-text-tertiary)" }}>beat</span> {r.loser}
                    </p>
                  ))}
                </div>
              ))}
            </div>
          )}

          {result.type === "survival" && (
            <div style={{ background: "var(--color-background-secondary)", borderRadius: "var(--border-radius-lg)", padding: "1.25rem", border: "0.5px solid var(--color-border-tertiary)" }}>
              <p style={{ margin: "0 0 8px", fontSize: 13, color: "var(--color-text-secondary)" }}>Survival arena</p>
              <p style={{ margin: "0 0 16px", fontSize: 20, fontWeight: 500 }}>🏆 Last survivor: {result.survivor}</p>
              {result.log.map((l, i) => (
                <p key={i} style={{ margin: "2px 0", fontSize: 13, color: "var(--color-text-secondary)" }}>
                  {l.fight} → <span style={{ color: "var(--color-text-primary)", fontWeight: 500 }}>{l.winner}</span>
                </p>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function QuotesTab() {
  const [theme, setTheme] = useState("Motivational");
  const [result, setResult] = useState(null);

  function generate() {
    const pool = QUOTES[theme];
    setResult(pool[Math.floor(Math.random() * pool.length)]);
  }

  return (
    <div>
      <h2 style={{ fontSize: 18, fontWeight: 500, marginBottom: "1rem" }}>Quote generator</h2>
      <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: "1.5rem" }}>
        {Object.keys(QUOTES).map(t => (
          <button key={t} onClick={() => { setTheme(t); setResult(null); }} style={{ background: theme === t ? "var(--color-background-secondary)" : "none", borderColor: theme === t ? "var(--color-border-primary)" : "var(--color-border-secondary)", fontWeight: theme === t ? 500 : 400 }}>
            {t}
          </button>
        ))}
      </div>
      <button onClick={generate} style={{ padding: "8px 24px", marginBottom: "1.5rem", fontWeight: 500 }}>Generate quote</button>

      {result && (
        <div style={{ background: "var(--color-background-secondary)", borderRadius: "var(--border-radius-lg)", padding: "1.5rem", border: "0.5px solid var(--color-border-tertiary)", maxWidth: 540 }}>
          <p style={{ margin: "0 0 12px", fontSize: 17, fontFamily: "var(--font-serif)", lineHeight: 1.6, color: "var(--color-text-primary)" }}>
            "{result.quote}"
          </p>
          <p style={{ margin: 0, fontSize: 13, color: "var(--color-text-secondary)" }}>— {result.char}</p>
        </div>
      )}
    </div>
  );
}

function QuizTab() {
  const QUESTIONS = [
    { key: "motivation", label: "What drives you most?", options: ["Power", "Friendship", "Freedom", "Knowledge"] },
    { key: "style", label: "How do you approach a fight?", options: ["Head on", "Strategic", "Support friends", "Adapt"] },
    { key: "trait", label: "Your defining trait?", options: ["Courage", "Intelligence", "Loyalty", "Calmness"] },
    { key: "role", label: "Your natural role?", options: ["Leader", "Support", "Lone wolf", "Strategist"] },
    { key: "weakness", label: "Your biggest weakness?", options: ["Anger", "Trust issues", "Overconfidence", "Fear"] },
    { key: "power", label: "Your power type?", options: ["Physical strength", "Speed", "Magic/Skills", "Tactical mind"] },
  ];

  const [answers, setAnswers] = useState({});
  const [result, setResult] = useState(null);

  function setAnswer(key, val) { setAnswers(p => ({ ...p, [key]: val })); }

  function reveal() {
    const vals = QUESTIONS.map(q => answers[q.key] || q.options[0]);
    setResult(getCharacterMatch(vals));
  }

  const allAnswered = QUESTIONS.every(q => answers[q.key]);

  return (
    <div>
      <h2 style={{ fontSize: 18, fontWeight: 500, marginBottom: "1rem" }}>Personality quiz</h2>
      <div style={{ display: "flex", flexDirection: "column", gap: "1.25rem", marginBottom: "1.5rem" }}>
        {QUESTIONS.map(q => (
          <div key={q.key}>
            <p style={{ margin: "0 0 8px", fontSize: 14, fontWeight: 500 }}>{q.label}</p>
            <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
              {q.options.map(opt => (
                <button key={opt} onClick={() => setAnswer(q.key, opt)} style={{
                  background: answers[q.key] === opt ? "var(--color-background-secondary)" : "none",
                  borderColor: answers[q.key] === opt ? "var(--color-border-primary)" : "var(--color-border-secondary)",
                  fontWeight: answers[q.key] === opt ? 500 : 400, fontSize: 13, padding: "5px 14px",
                }}>
                  {opt}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>

      <button onClick={reveal} style={{ padding: "8px 24px", fontWeight: 500 }}>
        Reveal my character
      </button>

      {result && (
        <div style={{ marginTop: "1.5rem", display: "flex", gap: "1.5rem", flexWrap: "wrap" }}>
          <img src={CHARACTER_IMAGES[result.winner]} alt={result.winner}
            style={{ width: 140, height: 180, objectFit: "cover", borderRadius: "var(--border-radius-lg)", border: "0.5px solid var(--color-border-tertiary)" }}
            onError={e => { e.target.style.display = "none"; }} />
          <div style={{ flex: 1, minWidth: 200 }}>
            <p style={{ margin: "0 0 4px", fontSize: 13, color: "var(--color-text-secondary)" }}>You are most like</p>
            <h3 style={{ margin: "0 0 8px", fontSize: 22, fontWeight: 500 }}>{result.winner}</h3>
            <p style={{ margin: "0 0 16px", fontSize: 14, color: "var(--color-text-secondary)", lineHeight: 1.6 }}>
              {CHARACTER_DESCRIPTIONS[result.winner]}
            </p>
            <p style={{ margin: "0 0 6px", fontSize: 13, fontWeight: 500 }}>Match breakdown</p>
            <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
              {Object.entries(result.percentages).sort((a, b) => b[1] - a[1]).slice(0, 5).map(([char, pct]) => (
                <div key={char} style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <span style={{ fontSize: 12, color: "var(--color-text-secondary)", minWidth: 130 }}>{char}</span>
                  <div style={{ flex: 1, background: "var(--color-background-secondary)", borderRadius: 999, height: 6, overflow: "hidden", border: "0.5px solid var(--color-border-tertiary)" }}>
                    <div style={{ width: `${pct}%`, background: char === result.winner ? "var(--color-text-primary)" : "var(--color-border-primary)", height: "100%", borderRadius: 999 }} />
                  </div>
                  <span style={{ fontSize: 12, color: "var(--color-text-secondary)", minWidth: 30, textAlign: "right" }}>{pct}%</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function LoginTab({ users, setUsers, loggedIn, setLoggedIn }) {
  const [screen, setScreen] = useState("login");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState({ text: "", type: "" });

  function register() {
    if (!username.trim() || !password.trim()) { setMsg({ text: "Fill in both fields.", type: "error" }); return; }
    if (users[username]) { setMsg({ text: "Username already taken.", type: "error" }); return; }
    setUsers(p => ({ ...p, [username]: password }));
    setMsg({ text: "Account created! You can now log in.", type: "success" });
    setScreen("login"); setUsername(""); setPassword("");
  }

  function login() {
    if (users[username] === password) {
      setLoggedIn(username); setMsg({ text: `Welcome, ${username}!`, type: "success" });
    } else {
      setMsg({ text: "Invalid username or password.", type: "error" });
    }
  }

  if (loggedIn) {
    return (
      <div>
        <h2 style={{ fontSize: 18, fontWeight: 500, marginBottom: "0.5rem" }}>Account</h2>
        <p style={{ color: "var(--color-text-secondary)", fontSize: 14 }}>Signed in as <strong style={{ fontWeight: 500, color: "var(--color-text-primary)" }}>{loggedIn}</strong></p>
        <button onClick={() => setLoggedIn(null)} style={{ marginTop: 8 }}>Sign out</button>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: 380 }}>
      <div style={{ display: "flex", gap: 8, marginBottom: "1.5rem" }}>
        {["login", "register"].map(s => (
          <button key={s} onClick={() => { setScreen(s); setMsg({ text: "", type: "" }); }} style={{
            background: screen === s ? "var(--color-background-secondary)" : "none",
            borderColor: screen === s ? "var(--color-border-primary)" : "var(--color-border-secondary)",
            fontWeight: screen === s ? 500 : 400, textTransform: "capitalize",
          }}>
            {s === "login" ? "Sign in" : "Register"}
          </button>
        ))}
      </div>

      <h2 style={{ fontSize: 18, fontWeight: 500, marginBottom: "1rem" }}>{screen === "login" ? "Sign in" : "Create account"}</h2>

      <div style={{ display: "flex", flexDirection: "column", gap: 10, marginBottom: 16 }}>
        <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" style={{ width: "100%" }} />
        <input value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" type="password" style={{ width: "100%" }}
          onKeyDown={e => e.key === "Enter" && (screen === "login" ? login() : register())} />
      </div>

      {msg.text && (
        <p style={{ fontSize: 13, margin: "0 0 12px", color: msg.type === "error" ? "var(--color-text-danger)" : "var(--color-text-success)" }}>{msg.text}</p>
      )}

      <button onClick={screen === "login" ? login : register} style={{ padding: "8px 24px", fontWeight: 500 }}>
        {screen === "login" ? "Sign in" : "Create account"}
      </button>
    </div>
  );
}
