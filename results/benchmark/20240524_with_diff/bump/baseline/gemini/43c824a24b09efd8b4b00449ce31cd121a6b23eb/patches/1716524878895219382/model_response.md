```java
import de.gwdg.metadataqa.api.json.DataElement;
import de.gwdg.metadataqa.api.json.JsonBranch;

public class MarcFactory {

    public static JsonBranch createMarcJsonBranch(String jsonPath, String label, String identifier, String indexField, String solrFieldName, boolean extractable, boolean mandatory, boolean collection, boolean active, List<JsonBranch> children, List<String> categories, List<Rule> rules, Schema schema) {
        JsonBranch branch = new JsonBranch(jsonPath, label, identifier);
        branch.setIndexField(indexField);
        branch.setSolrFieldName(solrFieldName);
        branch.setExtractable(extractable);
        branch.setMandatory(mandatory);
        branch.setCollection(collection);
        branch.setActive(active);
        branch.setChildren(children);
        branch.setCategories(categories);
        branch.setRules(rules);
        branch.setSchema(schema);
        return branch;
    }

    public static JsonBranch createMarcJsonBranch(String jsonPath, String label, String identifier, String indexField, String solrFieldName, boolean extractable, boolean mandatory, boolean collection, boolean active, List<JsonBranch> children, String[] categories, List<Rule> rules, Schema schema) {
        JsonBranch branch = new JsonBranch(jsonPath, label, identifier);
        branch.setIndexField(indexField);
        branch.setSolrFieldName(solrFieldName);
        branch.setExtractable(extractable);
        branch.setMandatory(mandatory);
        branch.setCollection(collection);
        branch.setActive(active);
        branch.setChildren(children);
        branch.setCategories(categories);
        branch.setRules(rules);
        branch.setSchema(schema);
        return branch;
    }

    public static JsonBranch createMarcJsonBranch(String jsonPath, String label, String identifier, String indexField, String solrFieldName, boolean extractable, boolean mandatory, boolean collection, boolean active, List<JsonBranch> children, List<DataElement> categories, List<Rule> rules, Schema schema) {
        JsonBranch branch = new JsonBranch(jsonPath, label, identifier);
        branch.setIndexField(indexField);
        branch.setSolrFieldName(solrFieldName);
        branch.setExtractable(extractable);
        branch.setMandatory(mandatory);
        branch.setCollection(collection);
        branch.setActive(active);
        branch.setChildren(children);
        branch.setCategories(categories);
        branch.setRules(rules);
        branch.setSchema(schema);
        return branch;
    }
}
```