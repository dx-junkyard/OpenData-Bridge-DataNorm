import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import ColumnsComponent from './components/Columns';
import { ColumnName, ColumnNames } from './components/Columns';


const App: React.FC = () => {
  const [columnsGroup, setColumnsGroup] = useState<ColumnNames[]>([]);

  const addGroup = (fileName : string) => {
    // 新しいColumnsオブジェクトを作成します（例として、空のオブジェクトを使用しますが、適切なデータに置き換えてください）
    const numberOfToggles = Math.floor(Math.random() * 5) + 1;
    const newColumns: ColumnName[] = Array.from({ length: numberOfToggles }, (_, i) => ({
      id: uuidv4(),
      isOn: false,
      name: `Column ${i}`
    }));
    const newGroup: ColumnNames = {
      id: uuidv4(),
      name: fileName,  // ダミーの名前。実際の名前を設定する必要があるかもしれません。
      columns: newColumns
    };
    setColumnsGroup(prevColumnsGroup => [...prevColumnsGroup, newGroup]);
  };

  return (
    <div>
      <input 
        type="file" 
        accept=".csv"
        multiple 
        onChange={(e) => {
          if (e.target.files && e.target.files.length > 0) {
            for (let i = 0; i < e.target.files.length; i++) {
              addGroup(e.target.files[i].name);
              console.log(e.target.files[i].name);
            } 
          }
        }}
      />
      <button>変換</button>      
      <ColumnsComponent columnNamesGroup={columnsGroup} setColumnsGroup={setColumnsGroup} />
    </div>
  );
};

export default App;