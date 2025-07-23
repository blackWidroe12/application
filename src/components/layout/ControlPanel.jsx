import React from 'react';
import InfrastructureFilter from '../filters/InfrastructureFilter';
import WardSelector from '../filters/WardSelector';
import QuickFilters from '../filters/QuickFilters';

const ControlPanel = () => (
  <aside className="control-panel">
    <div className="panel-header">
      <span>Filters & Tools</span>
    </div>
    <div className="panel-content">
      <WardSelector />
      <InfrastructureFilter />
      <QuickFilters />
    </div>
  </aside>
);

export default ControlPanel;
    </div>
  </aside>
);

export default ControlPanel;
