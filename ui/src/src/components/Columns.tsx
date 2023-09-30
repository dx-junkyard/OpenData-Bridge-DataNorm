import React from 'react';
import ToggleSwitch from './ToggleSwitch';

export type ColumnName = {
    id: string;
    isOn: boolean;
    name: string;
};

export type ColumnNames = {
    id: string;
    columns: ColumnName[];
    name: string;
};

type ColumnsProps = {
    columnNamesGroup: ColumnNames[];
    setColumnsGroup: React.Dispatch<React.SetStateAction<ColumnNames[]>>;
};

const ColumnsComponent: React.FC<ColumnsProps> = ({ columnNamesGroup, setColumnsGroup }) => {
    const handleToggle = (groupId: string, toggleId: string) => {
        console.log(groupId, toggleId);
        setColumnsGroup(columnNamesGroup.map(columnNames => 
            columnNames.id === groupId ? { 
                ...columnNames, 
                columns: columnNames.columns.map(toggle => 
                    toggle.id === toggleId ? { ...toggle, isOn: !toggle.isOn } : toggle
                )
            } : columnNames
        ));
    };

    const handleRemoveGroup = (groupId: string) => {
        // filter関数で指定されたIDのグループ以外のグループを残すことで、指定されたグループを削除
        setColumnsGroup(prevGroups => prevGroups.filter(group => group.id !== groupId));
    };


    return (
        <div>
            {columnNamesGroup.map(columnNames => (
                <div
                    key={columnNames.id}
                    className="group-container"
                    style={{ 
                    border: '1px solid black',  // これを追加
                    padding: '10px',  // 内部のスペースを少し追加
                    marginBottom: '10px',  // グループ間のスペースを追加
                    borderRadius: '5px'  // 枠線の角を少し丸くする
                    }}
                >

                    <span className="group-name">{columnNames.name}</span>
                    <div style={{ display: 'flex', gap: '10px'}}>
                        {columnNames.columns.map(columnName => (
                            <div className="toggle-item" key={columnName.id}>
                                <ToggleSwitch
                                    isOn={columnName.isOn}
                                    handleToggle={() => handleToggle(columnNames.id, columnName.id)}
                                    label={columnName.name}
                                />

                            </div>
                        ))}
                        <button onClick={() => handleRemoveGroup(columnNames.id)}>削除</button>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default ColumnsComponent;
