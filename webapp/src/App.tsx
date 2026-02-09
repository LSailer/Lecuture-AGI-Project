import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { LandingPage } from './components/pages/LandingPage';
import { ExperimentPage } from './components/pages/ExperimentPage';
import { loadExperiments } from './data';

// Load all experiments at app initialization
const experiments = loadExperiments();

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage experiments={experiments} />} />
        <Route path="/experiment/:filename" element={<ExperimentPage experiments={experiments} />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
