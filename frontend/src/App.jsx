import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Target, Activity, Zap, ShieldCheck, Cpu, MessageSquare, Briefcase, Network, HeadphonesIcon, User, Monitor } from 'lucide-react';
import axios from 'axios';
import './index.css';

const SHAPBar = ({ feature, value, maxVal, index }) => {
  const isPositive = value > 0;
  const color = isPositive ? 'var(--red-glow)' : 'var(--green-glow)'; 
  const widthPercentage = Math.min((Math.abs(value) / maxVal) * 100, 100);

  return (
    <motion.div 
      initial={{ opacity: 0, x: -30 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.6, delay: index * 0.15 }}
      className="shap-item"
    >
      <div className="shap-header">
        <span className="shap-label">
          <Zap size={14} color="var(--gold-primary)" /> {feature.replace(/_/g, ' ')}
        </span>
        <span className="shap-val" style={{ color }}>{value.toFixed(3)}</span>
      </div>
      <div className="shap-track">
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${widthPercentage}%` }}
          transition={{ duration: 1.5, ease: [0.16, 1, 0.3, 1], delay: index * 0.1 + 0.3 }}
          style={{ height: '100%', backgroundColor: color, boxShadow: `0 0 10px ${color}` }}
        />
      </div>
    </motion.div>
  );
};

function App() {
  const [profile, setProfile] = useState({
    age: 35,
    tenure_months: 12,
    contract_type: 0,
    monthly_charges: 85.0,
    total_charges: 1020.0,
    tech_savvy: 1,
    support_tickets: 2,
    recent_network_drops: 5
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [activeStep, setActiveStep] = useState(0);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfile(prev => ({
      ...prev,
      [name]: parseFloat(value),
      total_charges: name === 'tenure_months' || name === 'monthly_charges' 
        ? (name === 'tenure_months' ? value * prev.monthly_charges : prev.tenure_months * value)
        : prev.total_charges
    }));
  };

  const runWorkflow = async () => {
    setLoading(true);
    setResult(null);
    setActiveStep(1);

    try {
      const interval = setInterval(() => {
        setActiveStep(prev => (prev < 5 ? prev + 1 : prev));
      }, 800);

      const res = await axios.post('/api/v1/run-agents', {
        customer_id: `CUST_${Date.now()}`,
        ...profile
      });

      clearInterval(interval);
      setActiveStep(5);
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("API Connection Error. Please verify the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  const steps = ["Acquisition", "Predictive Risk", "XAI Analysis", "Strategy Setup", "Deployment"];

  return (
    <div className="app-container">
      
      <motion.header 
        initial={{ y: -30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 1 }}
        className="header"
      >
        <div className="glow-orb" />
        <Target size={40} color="var(--gold-primary)" style={{ marginBottom: '20px' }} />
        <h1>Retention Intelligence</h1>
        <div className="subtitle-line" />
      </motion.header>

      <div className="dashboard-grid">
        
        <motion.div 
          className="premium-box" style={{ alignSelf: 'start' }}
          initial={{ x: -40, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ duration: 0.8 }}
        >
          <div className="section-title">Client Profile Parameter</div>
          
          <div className="form-section">
            <div className="form-row">
              <div className="input-container">
                <label><User size={14} color="var(--gold-primary)"/> Age</label>
                <input type="number" name="age" value={profile.age} onChange={handleInputChange} />
              </div>
              <div className="input-container">
                <label><Monitor size={14} color="var(--gold-primary)"/> Tech</label>
                <select name="tech_savvy" value={profile.tech_savvy} onChange={handleInputChange}>
                  <option value="1">Yes</option>
                  <option value="0">No</option>
                </select>
              </div>
            </div>

            <div className="input-container">
              <label>Lifecycle Tenure ({profile.tenure_months} Mo)</label>
              <input type="range" name="tenure_months" min="1" max="72" value={profile.tenure_months} onChange={handleInputChange} />
            </div>

            <div className="input-container">
              <label>Service Agreement</label>
              <div style={{position: 'relative'}}>
                <Briefcase size={16} color="var(--gold-primary)" style={{position: 'absolute', left: '16px', top: '16px'}} />
                <select name="contract_type" value={profile.contract_type} onChange={handleInputChange} style={{paddingLeft: '40px'}}>
                  <option value="0">Basic / Month-to-Month</option>
                  <option value="1">Standard / Annual</option>
                  <option value="2">Premium / Bi-Annual</option>
                </select>
              </div>
            </div>

            <div className="form-row">
              <div className="input-container">
                <label>Monthly ($)</label>
                <input type="number" name="monthly_charges" value={profile.monthly_charges} onChange={handleInputChange} />
              </div>
              <div className="input-container">
                <label>Total LTV Auto</label>
                <input type="text" className="readonly-input" value={`$ ${profile.total_charges.toFixed(2)}`} readOnly />
              </div>
            </div>

            <div className="form-row">
              <div className="input-container">
                <label><HeadphonesIcon size={14} style={{display:'inline-block', verticalAlign:'middle'}}/> Tickets</label>
                <input type="number" name="support_tickets" value={profile.support_tickets} onChange={handleInputChange} />
              </div>
              <div className="input-container">
                <label><Network size={14} style={{display:'inline-block', verticalAlign:'middle'}}/> Drops</label>
                <input type="number" name="recent_network_drops" value={profile.recent_network_drops} onChange={handleInputChange} />
              </div>
            </div>
          </div>

          <button 
            className="btn-engage"
            onClick={runWorkflow}
            disabled={loading}
          >
            {loading ? "Synthesizing AI Core..." : "Initialize AI Framework"}
          </button>
        </motion.div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '40px' }}>
          
          <motion.div 
             initial={{ opacity: 0 }}
             animate={{ opacity: 1 }}
             transition={{ delay: 0.4, duration: 1 }}
             className="premium-box" style={{ padding: '0' }}
          >
            <div className="pipeline-container">
              <div className="pipeline-line" />
              <div 
                className="pipeline-progress" 
                style={{ width: `${(Math.max(activeStep - 1, 0) / (steps.length - 1)) * 100}%` }} 
              />

              {steps.map((label, idx) => {
                const isActive = activeStep > idx;
                const isCurrent = activeStep === idx + 1;
                return (
                  <div key={idx} className="pipeline-node">
                    <div className={`node-circle ${isActive ? 'active' : ''}`} style={isCurrent ? { transform: 'scale(1.5)', background: 'var(--gold-dark)' } : {}} />
                    <span className={`node-label ${isActive ? 'active' : ''}`}>{label}</span>
                  </div>
                );
              })}
            </div>
          </motion.div>

          <AnimatePresence mode="wait">
            {result && (
              <motion.div 
                key="results"
                className="results-grid"
                variants={{
                  hidden: { opacity: 0 },
                  show: { opacity: 1, transition: { staggerChildren: 0.25 } }
                }}
                initial="hidden"
                animate="show"
              >
                
                <motion.div variants={{ hidden: { opacity: 0, scale: 0.95 }, show: { opacity: 1, scale: 1 } }} className="premium-box" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                  <ShieldCheck size={40} color="var(--gold-primary)" />
                  <h3 className="section-title" style={{ marginTop: '20px', marginBottom: '0', justifyContent: 'center' }}>
                    <span className="text-gold-gradient">Predicted Risk Profile</span>
                  </h3>
                  <div className={`value-highlight ${result.risk_score > 0.6 ? 'danger' : ''}`}>
                    {(result.risk_score * 100).toFixed(1)}%
                  </div>
                  <div className="badge">
                    {result.risk_category} Level
                  </div>
                </motion.div>

                <motion.div variants={{ hidden: { opacity: 0, x: 20 }, show: { opacity: 1, x: 0 } }} className="premium-box">
                  <h3 className="section-title"><Cpu color="var(--gold-primary)" /> Explainable AI Matrix</h3>
                  <div style={{ marginTop: '30px' }}>
                    {Object.entries(result.shap_values)
                      .sort(([, a], [, b]) => Math.abs(b) - Math.abs(a))
                      .slice(0, 4)
                      .map(([feature, value], index) => (
                      <SHAPBar key={feature} feature={feature} value={value} maxVal={1.5} index={index} />
                    ))}
                  </div>
                </motion.div>

                <motion.div variants={{ hidden: { opacity: 0, y: 20 }, show: { opacity: 1, y: 0 } }} className="premium-box card-full">
                  <h3 className="section-title"><Activity color="var(--gold-primary)" /> Tactical Strategy AI</h3>
                  <div className="strategy-layout">
                    <div className="action-box">
                      <div className="action-label">Approved Action</div>
                      <div className="action-value">{result.action_type.replace(/_/g, ' ')}</div>
                    </div>
                    <div className="reasoning-text">
                      {result.strategy_reasoning}
                    </div>
                    
                    <div className="sim-delta-box">
                      <div className="action-label" style={{ color: 'var(--green-glow)' }}>Post-Simulated Risk</div>
                      <div className="value-highlight success" style={{ fontSize: '3rem', margin: '10px 0' }}>
                        {(result.simulated_outcome_prob * 100).toFixed(1)}%
                      </div>
                      <span className="badge" style={{ borderColor: 'var(--green-glow)', color: 'var(--green-glow)' }}>
                        ↓ {((result.risk_score - result.simulated_outcome_prob)*100).toFixed(1)}% Drop
                      </span>
                    </div>
                  </div>
                </motion.div>

                <motion.div variants={{ hidden: { opacity: 0, y: 20 }, show: { opacity: 1, y: 0 } }} className="premium-box card-full">
                  <h3 className="section-title"><MessageSquare color="var(--gold-primary)" /> Autonomous Dispatch Draft</h3>
                  <div className="comms-block">
                    <div style={{ position: 'absolute', top: '20px', left: '20px', fontSize: '6rem', color: 'rgba(212,175,55,0.2)', fontFamily: 'Cormorant Garamond', lineHeight: 1 }}>"</div>
                    <p className="comms-quote">{result.drafted_message}</p>
                    <div style={{ marginTop: '30px', textAlign: 'right' }}>
                      <span className="badge" style={{ color: 'var(--gold-primary)', borderColor: 'var(--gold-primary)' }}>Agent Generated Payload</span>
                    </div>
                  </div>
                </motion.div>

              </motion.div>
            )}
          </AnimatePresence>

        </div>
      </div>
    </div>
  );
}

export default App;
