```java
import de.gwdg.metadataqa.api.json.JsonBranch;
import org.marc4j.marc.Record;

public class MarcFactory {

    private static final String MARC_FORMAT = "MARC";

    public static Record createRecord(JsonBranch jsonBranch) {
        Record record = new Record();
        record.setLeader(jsonBranch.getLeader());
        record.setControlFields(jsonBranch.getControlFields());
        record.setDataFields(jsonBranch.getDataFields());
        return record;
    }

    public static String getFormat() {
        return MARC_FORMAT;
    }
}
```