```java
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonEntry;
  import de.gwdg.metadataqa.api.json.JsonEntryType;
  import de.gwdg.metadataqa.api.json.JsonField;
  import de.gwdg.metadataqa.api.json.JsonSubEntry;
  import de.gwdg.metadataqa.api.json.JsonSubEntryType;
  import de.gwdg.metadataqa.api.json.JsonUtils;
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonEntry;
  import de.gwdg.metadataqa.api.json.JsonEntryType;
  import de.gwdg.metadataqa.api.json.JsonField;
  import de.gwdg.metadataqa.api.json.JsonSubEntry;
  import de.gwdg.metadataqa.api.json.JsonSubEntryType;
  import de.gwdg.metadataqa.api.json.JsonUtils;
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonEntry;
  import de.gwdg.metadataqa.api.json.JsonEntryType;
  import de.gwdg.metadataqa.api.json.JsonField;
  import de.gwdg.metadataqa.api.json.JsonSubEntry;
  import de.gwdg.metadataqa.api.json.JsonSubEntryType;
  import de.gwdg.metadataqa.api.json.JsonUtils;
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonEntry;
  import de.gwdg.metadataqa.api.json.JsonEntryType;
  import de.gwdg.metadataqa.api.json.JsonField;
  import de.gwdg.metadataqa.api.json.JsonSubEntry;
  import de.gwdg.metadataqa.api.json.JsonSubEntryType;
  import de.gwdg.metadataqa.api.json.JsonUtils;
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonEntry;
  import de.gwdg.metadataqa.api.json.JsonEntryType;
  import de.gwdg.metadataqa.api.json.JsonField;
  import de.gwdg.metadataqa.api.json.JsonSubEntry;
  import de.gwdg.metadataqa.api.json.JsonSubEntryType;
  import de.gwdg.metadataqa.api.json.JsonUtils;
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonEntry;
  import de.gwdg.metadataqa.api.json.JsonEntryType;
  import de.gwdg.metadataqa.api.json.JsonField;
  import de.gwdg.metadataqa.api.json.JsonSubEntry;
  import de.gwdg.metadataqa.api.json.JsonSubEntryType;
  import de.gwdg.metadataqa.api.json.JsonUtils;

  import java.util.ArrayList;
  import java.util.List;
  import java.util.Map;
  import java.util.Optional;
  import java.util.stream.Collectors;

  import org.apache.commons.lang3.StringUtils;
  import org.apache.commons.lang3.tuple.Pair;
  import org.apache.logging.log4j.LogManager;
  import org.apache.logging.log4j.Logger;
  import org.json.JSONObject;

  /**
   * This class is used to create a MARC record from a JSON object.
   *
   * @author Michael Gleeson
   */
  public class MarcFactory {

    private static final Logger LOGGER = LogManager.getLogger(MarcFactory.class);

    private static final String MARC_LEADER = "LEADER";
    private static final String MARC_CONTROL_FIELD = "CONTROL_FIELD";
    private static final String MARC_DATA_FIELD = "DATA_FIELD";
    private static final String MARC_SUBFIELD = "SUBFIELD";

    private static final String MARC_LEADER_CHARACTERS = "00000nam a2200000ma 4500";

    private static final String MARC_FIELD_TAG = "tag";
    private static final String MARC_FIELD_IND1 = "ind1";
    private static final String MARC_FIELD_IND2 = "ind2";
    private static final String MARC_FIELD_SUBFIELDS = "subfields";

    private static final String MARC_SUBFIELD_CODE = "code";
    private static final String MARC_SUBFIELD_VALUE = "value";

    /**
     * Creates a MARC record from a JSON object.
     *
     * @param jsonObject The JSON object to create the MARC record from.
     * @return The MARC record.
     */
    public static String createMarcRecord(JSONObject jsonObject) {
      // Get the MARC leader.
      String marcLeader = getMarcLeader(jsonObject);

      // Get the MARC control fields.
      List<String> marcControlFields = getMarcControlFields(jsonObject);

      // Get the MARC data fields.
      List<String> marcDataFields = getMarcDataFields(jsonObject);

      // Combine the MARC leader, control fields, and data fields into a single string.
      StringBuilder marcRecord = new StringBuilder();
      marcRecord.append(marcLeader);
      marcRecord.append(String.join("", marcControlFields));
      marcRecord.append(String.join("", marcDataFields));

      return marcRecord.toString();
    }

    /**
     * Gets the MARC leader from a JSON object.
     *
     * @param jsonObject The JSON object to get the MARC leader from.
     * @return The MARC leader.
     */
    private static String getMarcLeader(JSONObject jsonObject) {
      return MARC_LEADER_CHARACTERS;
    }

    /**
     * Gets the MARC control fields from a JSON object.
     *
     * @param jsonObject The JSON object to get the MARC control fields from.
     * @return The MARC control fields.
     */
    private static List<String> getMarcControlFields(JSONObject jsonObject) {
      List<String> marcControlFields = new ArrayList<>();

      // Get the control fields from the JSON object.
      Map<String, Object> controlFields = jsonObject.getJSONObject(MARC_CONTROL_FIELD).toMap();

      // Iterate over the control fields and create a MARC control field for each one.
      for (Map.Entry<String, Object> entry : controlFields.entrySet()) {
        String tag = entry.getKey();
        String value = entry.getValue().toString();

        // Create a MARC control field.
        String marcControlField = String.format("%-3s %-1s %-1s %s", tag, value.substring(0, 1), value.substring(1), StringUtils.repeat(' ', 17));

        // Add the MARC control field to the list.
        marcControlFields.add(marcControlField);
      }

      return marcControlFields;
    }

    /**
     * Gets the MARC data fields from a JSON object.
     *
     * @param jsonObject The JSON object to get the MARC data fields from.
     * @return The MARC data fields.
     */
    private static List<String> getMarcDataFields(JSONObject jsonObject) {
      List<String> marcDataFields = new ArrayList<>();

      // Get the data fields from the JSON object.
      List<Object> dataFields = jsonObject.getJSONArray(MARC_DATA_FIELD).toList();

      // Iterate over the data fields and create a MARC data field for each one.
      for (Object dataFieldObject : dataFields) {
        JSONObject dataField = (JSONObject) dataFieldObject;

        // Get the tag, ind1, ind2, and subfields from the data field.
        String tag = dataField.getString(MARC_FIELD_TAG);
        String ind1 = dataField.getString(MARC_FIELD_IND1);
        String ind2 = dataField.getString(MARC_FIELD_IND2);
        List<Object> subfields = dataField.getJSONArray(MARC_FIELD_SUBFIELDS).toList();

        // Create a MARC data field.
        String marcDataField = String.format("%-3s %-1s %-1s %s", tag, ind1, ind2, createMarcSubfields(subfields));

        // Add the MARC data field to the list.
        marcDataFields.add(marcDataField);
      }

      return marcDataFields;
    }

    /**
     * Creates the MARC subfields from a list of subfield objects.
     *
     * @param subfields The list of subfield objects.
     * @return The MARC subfields.
     */
    private static String createMarcSubfields(List<Object> subfields) {
      StringBuilder marcSubfields = new StringBuilder();

      // Iterate over the subfields and create a MARC subfield for each one.
      for (Object subfieldObject : subfields) {
        JSONObject subfield = (JSONObject) subfieldObject;

        // Get the code and value from the subfield.
        String code = subfield.getString(MARC_SUBFIELD_CODE);
        String value = subfield.getString(MARC_SUBFIELD_VALUE);

        // Create a MARC subfield.
        String marcSubfield = String.format("%s%s", code, value);

        // Add the MARC subfield to the StringBuilder.
        marcSubfields.append(marcSubfield);
      }

      return marcSubfields.toString();
    }
  }
```