```java
import de.gwdg.metadataqa.api.json.DataElement;

import java.util.List;

public class MarcFactory {

    public static DataElement createMarcJsonSchema() {
        DataElement root = new DataElement("record");
        root.setCollection(true);
        root.setExtractable();

        DataElement leader = new DataElement("leader");
        leader.setCollection(true);
        leader.setExtractable();
        root.addChild(leader);

        DataElement controlFields = new DataElement("controlFields");
        controlFields.setCollection(true);
        controlFields.setExtractable();
        root.addChild(controlFields);

        DataElement dataFields = new DataElement("dataFields");
        dataFields.setCollection(true);
        dataFields.setExtractable();
        root.addChild(dataFields);

        return root;
    }
}
```