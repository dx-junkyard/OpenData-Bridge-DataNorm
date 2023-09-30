
import React from 'react';

interface Props {
  isOn: boolean;
  handleToggle: () => void;
  label: string;
}

const ToggleSwitch: React.FC<Props> = ({ isOn, handleToggle, label }) => {
  return (
    <button 
      onClick={handleToggle} 
      style={{
        backgroundColor: isOn ? 'cyan' : 'white', // ここで背景色を設定します。'cyan'は適当な色なので、お好きな色に変更できます。
        padding: '10px 20px',
        border: '1px solid gray',
        borderRadius: '4px',
        cursor: 'pointer'
      }}
    >
      {label}
    </button>
  );
}

export default ToggleSwitch;