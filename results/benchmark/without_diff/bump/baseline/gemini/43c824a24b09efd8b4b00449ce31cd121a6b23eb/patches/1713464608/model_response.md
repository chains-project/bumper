```java
import de.gwdg.metadataqa.api.json.JsonBranch;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class MarcFactory {

    private final MarcRecordFactory marcRecordFactory;

    public MarcFactory(MarcRecordFactory marcRecordFactory) {
        this.marcRecordFactory = marcRecordFactory;
    }

    public Optional<MarcRecord> createMarcRecord(JsonBranch branch) {
        // Create a new MARC record
        MarcRecord marcRecord = marcRecordFactory.newRecord();

        // Set the record leader
        marcRecord.setLeader(branch.getLeader());

        // Set the control fields
        List<ControlField> controlFields = branch.getControlFields().stream()
                .map(controlField -> new ControlField(controlField.getTag(), controlField.getValue()))
                .collect(Collectors.toList());
        marcRecord.setControlFields(controlFields);

        // Set the data fields
        List<DataField> dataFields = branch.getDataFields().stream()
                .map(dataField -> new DataField(dataField.getTag(), dataField.getSubfields()))
                .collect(Collectors.toList());
        marcRecord.setDataFields(dataFields);

        return Optional.of(marcRecord);
    }
}
```