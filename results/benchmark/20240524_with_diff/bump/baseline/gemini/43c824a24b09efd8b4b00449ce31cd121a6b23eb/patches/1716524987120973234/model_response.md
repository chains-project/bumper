```java
  import de.gwdg.metadataqa.api.json.DataElement;

  import java.util.List;

  public class MarcFactory {

    public static DataElement createMarcJsonBranch(String label) {
      DataElement dataElement = new DataElement(label);
      dataElement.setCollection(true);
      return dataElement;
    }

    public static DataElement createMarcJsonBranch(String label, DataElement parent, String path) {
      DataElement dataElement = new DataElement(label);
      dataElement.setParent(parent);
      dataElement.setJsonPath(path);
      return dataElement;
    }

    public static DataElement createMarcJsonBranch(String label, String path) {
      DataElement dataElement = new DataElement(label);
      dataElement.setJsonPath(path);
      return dataElement;
    }

    public static DataElement createMarcJsonBranch(String label, String path, String solrFieldName) {
      DataElement dataElement = new DataElement(label);
      dataElement.setJsonPath(path);
      dataElement.setSolrFieldName(solrFieldName);
      return dataElement;
    }

    public static DataElement createMarcJsonBranch(String label, List<String> categories) {
      DataElement dataElement = new DataElement(label);
      dataElement.setCategories(categories);
      return dataElement;
    }
  }
```