```java
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonDocument;
  import de.gwdg.metadataqa.api.json.JsonDocumentBuilder;
  import de.gwdg.metadataqa.api.json.JsonPath;
  import de.gwdg.metadataqa.api.json.JsonRoot;
  import de.gwdg.metadataqa.api.json.JsonString;
  import de.gwdg.metadataqa.api.json.JsonType;
  import de.gwdg.metadataqa.api.json.JsonUtils;
  import de.gwdg.metadataqa.api.json.JsonUtils.JsonUtilsException;
  import de.gwdg.metadataqa.api.json.JsonUtils.JsonUtilsException;
  import de.gwdg.metadataqa.api.json.JsonUtils.JsonUtilsException;
  import org.slf4j.Logger;
  import org.slf4j.LoggerFactory;

  import java.io.IOException;
  import java.io.InputStream;
  import java.io.InputStreamReader;
  import java.io.Reader;
  import java.nio.charset.Charset;
  import java.nio.charset.StandardCharsets;
  import java.util.ArrayList;
  import java.util.Arrays;
  import java.util.Collection;
  import java.util.Collections;
  import java.util.HashSet;
  import java.util.List;
  import java.util.Map;
  import java.util.Optional;
  import java.util.Set;
  import java.util.function.Function;
  import java.util.stream.Collectors;
  import java.util.stream.Stream;

  /**
   * Factory for creating {@link JsonDocument} instances.
   */
  public class MarcFactory {

    private static final Logger log = LoggerFactory.getLogger(MarcFactory.class);

    private static final String MARC_XML_HEADER = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>";
    private static final String MARC_XML_ROOT_ELEMENT = "record";
    private static final String MARC_XML_LEADER_ELEMENT = "leader";
    private static final String MARC_XML_CONTROL_FIELD_ELEMENT = "controlfield";
    private static final String MARC_XML_DATA_FIELD_ELEMENT = "datafield";
    private static final String MARC_XML_SUBFIELD_ELEMENT = "subfield";

    private static final String MARC_XML_LEADER_LENGTH = "24";
    private static final String MARC_XML_CONTROL_FIELD_TAG_LENGTH = "3";
    private static final String MARC_XML_CONTROL_FIELD_VALUE_LENGTH = "不定長";
    private static final String MARC_XML_DATA_FIELD_TAG_LENGTH = "3";
    private static final String MARC_XML_DATA_FIELD_INDICATOR_LENGTH = "2";
    private static final String MARC_XML_SUBFIELD_CODE_LENGTH = "1";
    private static final String MARC_XML_SUBFIELD_VALUE_LENGTH = "不定長";

    private static final Charset MARC_XML_CHARSET = StandardCharsets.UTF_8;

    private static final String MARC_XML_LEADER_PATTERN = "[0-9]{" + MARC_XML_LEADER_LENGTH + "}";
    private static final String MARC_XML_CONTROL_FIELD_PATTERN = "[0-9]{" + MARC_XML_CONTROL_FIELD_TAG_LENGTH + "}[^0-9]+";
    private static final String MARC_XML_DATA_FIELD_PATTERN = "[0-9]{" + MARC_XML_DATA_FIELD_TAG_LENGTH + "}[^0-9]{" + MARC_XML_DATA_FIELD_INDICATOR_LENGTH + "}";
    private static final String MARC_XML_SUBFIELD_PATTERN = "[A-Z]{" + MARC_XML_SUBFIELD_CODE_LENGTH + "}[^A-Z]+";

    private static final String MARC_XML_LEADER_GROUP_PATTERN = "[0-9]{" + MARC_XML_LEADER_LENGTH + "}(?=</" + MARC_XML_ROOT_ELEMENT + ">)";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_PATTERN = "[0-9]{" + MARC_XML_CONTROL_FIELD_TAG_LENGTH + "}[^0-9]+(?=</" + MARC_XML_ROOT_ELEMENT + ">)";
    private static final String MARC_XML_DATA_FIELD_GROUP_PATTERN = "[0-9]{" + MARC_XML_DATA_FIELD_TAG_LENGTH + "}[^0-9]{" + MARC_XML_DATA_FIELD_INDICATOR_LENGTH + "}(?=</" + MARC_XML_ROOT_ELEMENT + ">)";
    private static final String MARC_XML_SUBFIELD_GROUP_PATTERN = "[A-Z]{" + MARC_XML_SUBFIELD_CODE_LENGTH + "}[^A-Z]+(?=</" + MARC_XML_ROOT_ELEMENT + ">)";

    private static final String MARC_XML_LEADER_SEPARATOR = "";
    private static final String MARC_XML_CONTROL_FIELD_SEPARATOR = "";
    private static final String MARC_XML_DATA_FIELD_SEPARATOR = "";
    private static final String MARC_XML_SUBFIELD_SEPARATOR = "";

    private static final String MARC_XML_LEADER_GROUP_START = "<" + MARC_XML_ROOT_ELEMENT + "><" + MARC_XML_LEADER_ELEMENT + ">";
    private static final String MARC_XML_LEADER_GROUP_END = "</" + MARC_XML_LEADER_ELEMENT + ">";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_START = "<" + MARC_XML_ROOT_ELEMENT + "><" + MARC_XML_CONTROL_FIELD_ELEMENT + " tag=\"";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_END = "\"/></" + MARC_XML_ROOT_ELEMENT + ">";
    private static final String MARC_XML_DATA_FIELD_GROUP_START = "<" + MARC_XML_ROOT_ELEMENT + "><" + MARC_XML_DATA_FIELD_ELEMENT + " tag=\"";
    private static final String MARC_XML_DATA_FIELD_GROUP_END = "\"/></" + MARC_XML_ROOT_ELEMENT + ">";
    private static final String MARC_XML_SUBFIELD_GROUP_START = "<" + MARC_XML_ROOT_ELEMENT + "><" + MARC_XML_SUBFIELD_ELEMENT + " code=\"";
    private static final String MARC_XML_SUBFIELD_GROUP_END = "\"/></" + MARC_XML_ROOT_ELEMENT + ">";

    private static final String MARC_XML_LEADER_GROUP_START_PATTERN = "<" + MARC_XML_ROOT_ELEMENT + "><" + MARC_XML_LEADER_ELEMENT + ">";
    private static final String MARC_XML_LEADER_GROUP_END_PATTERN = "</" + MARC_XML_LEADER_ELEMENT + ">";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_START_PATTERN = "<" + MARC_XML_ROOT_ELEMENT + "><" + MARC_XML_CONTROL_FIELD_ELEMENT + " tag=\"";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_END_PATTERN = "\"/></" + MARC_XML_ROOT_ELEMENT + ">";
    private static final String MARC_XML_DATA_FIELD_GROUP_START_PATTERN = "<" + MARC_XML_ROOT_ELEMENT + "><" + MARC_XML_DATA_FIELD_ELEMENT + " tag=\"";
    private static final String MARC_XML_DATA_FIELD_GROUP_END_PATTERN = "\"/></" + MARC_XML_ROOT_ELEMENT + ">";
    private static final String MARC_XML_SUBFIELD_GROUP_START_PATTERN = "<" + MARC_XML_ROOT_ELEMENT + "><" + MARC_XML_SUBFIELD_ELEMENT + " code=\"";
    private static final String MARC_XML_SUBFIELD_GROUP_END_PATTERN = "\"/></" + MARC_XML_ROOT_ELEMENT + ">";

    private static final String MARC_XML_LEADER_GROUP_END_REPLACEMENT = "</" + MARC_XML_ROOT_ELEMENT + ">";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_END_REPLACEMENT = "</" + MARC_XML_ROOT_ELEMENT + ">";
    private static final String MARC_XML_DATA_FIELD_GROUP_END_REPLACEMENT = "</" + MARC_XML_ROOT_ELEMENT + ">";
    private static final String MARC_XML_SUBFIELD_GROUP_END_REPLACEMENT = "</" + MARC_XML_ROOT_ELEMENT + ">";

    private static final String MARC_XML_LEADER_GROUP_START_REPLACEMENT = "";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_START_REPLACEMENT = "";
    private static final String MARC_XML_DATA_FIELD_GROUP_START_REPLACEMENT = "";
    private static final String MARC_XML_SUBFIELD_GROUP_START_REPLACEMENT = "";

    private static final String MARC_XML_LEADER_GROUP_END_PATTERN_REPLACEMENT = "";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_END_PATTERN_REPLACEMENT = "";
    private static final String MARC_XML_DATA_FIELD_GROUP_END_PATTERN_REPLACEMENT = "";
    private static final String MARC_XML_SUBFIELD_GROUP_END_PATTERN_REPLACEMENT = "";

    private static final String MARC_XML_LEADER_GROUP_START_PATTERN_REPLACEMENT = "";
    private static final String MARC_XML_CONTROL_FIELD_GROUP_START_PATTERN_REPLACEMENT = "";
    private static final String MARC_XML_DATA_FIELD_GROUP_START_PATTERN_REPLACEMENT = "";
    private static final String MARC_XML_SUBFIELD_GROUP_START_PATTERN_REPLACEMENT = "";

    /**
     * Creates a new {@link JsonDocument} instance from the given MARC XML input stream.
     *
     * @param inputStream the MARC XML input stream
     * @return the new {@link JsonDocument} instance
     * @throws IOException if an error occurs while reading the input stream
     */
    public static JsonDocument createJsonDocument(InputStream inputStream) throws IOException {
      try (Reader reader = new InputStreamReader(inputStream, MARC_XML_CHARSET)) {
        String marcXml = JsonUtils.readToString(reader);

        // Remove MARC XML header
        marcXml = marcXml.substring(MARC_XML_HEADER.length());

        // Replace group start and end tags with empty strings
        marcXml = marcXml.replaceAll(MARC_XML_LEADER_GROUP_START_PATTERN, MARC_XML_LEADER_GROUP_START_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_LEADER_GROUP_END_PATTERN, MARC_XML_LEADER_GROUP_END_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_CONTROL_FIELD_GROUP_START_PATTERN, MARC_XML_CONTROL_FIELD_GROUP_START_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_CONTROL_FIELD_GROUP_END_PATTERN, MARC_XML_CONTROL_FIELD_GROUP_END_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_DATA_FIELD_GROUP_START_PATTERN, MARC_XML_DATA_FIELD_GROUP_START_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_DATA_FIELD_GROUP_END_PATTERN, MARC_XML_DATA_FIELD_GROUP_END_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_SUBFIELD_GROUP_START_PATTERN, MARC_XML_SUBFIELD_GROUP_START_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_SUBFIELD_GROUP_END_PATTERN, MARC_XML_SUBFIELD_GROUP_END_REPLACEMENT);

        // Replace group end tags with group end replacements
        marcXml = marcXml.replaceAll(MARC_XML_LEADER_GROUP_END_PATTERN, MARC_XML_LEADER_GROUP_END_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_CONTROL_FIELD_GROUP_END_PATTERN, MARC_XML_CONTROL_FIELD_GROUP_END_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_DATA_FIELD_GROUP_END_PATTERN, MARC_XML_DATA_FIELD_GROUP_END_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_SUBFIELD_GROUP_END_PATTERN, MARC_XML_SUBFIELD_GROUP_END_REPLACEMENT);

        // Replace group start tags with group start replacements
        marcXml = marcXml.replaceAll(MARC_XML_LEADER_GROUP_START_PATTERN, MARC_XML_LEADER_GROUP_START_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_CONTROL_FIELD_GROUP_START_PATTERN, MARC_XML_CONTROL_FIELD_GROUP_START_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_DATA_FIELD_GROUP_START_PATTERN, MARC_XML_DATA_FIELD_GROUP_START_REPLACEMENT);
        marcXml = marcXml.replaceAll(MARC_XML_SUBFIELD_GROUP_START_PATTERN, MARC_XML_SUBFIELD_GROUP_START_REPLACEMENT);

        // Split MARC XML into groups
        List<String> groups = Arrays.asList(marcXml.split(MARC_XML_ROOT_ELEMENT));

        // Create JSON document builder
        JsonDocumentBuilder builder = JsonDocument.builder();

        // Process groups
        groups.forEach(group -> {
          // Get group type
          String groupType = group.substring(0, group.indexOf(">"));

          // Process group based on type
          switch (groupType) {
            case MARC_XML_LEADER_ELEMENT:
              processLeaderGroup(builder, group);
              break;
            case MARC_XML_CONTROL_FIELD_ELEMENT:
              processControlFieldGroup(builder, group);
              break;
            case MARC_XML_DATA_FIELD_ELEMENT:
              processDataFieldGroup(builder, group);
              break;
            default:
              log.warn("Unknown group type: {}", groupType);
          }
        });

        // Build JSON document
        return builder.build();
      }
    }

    /**
     * Processes a leader group.
     *
     * @param builder the JSON document builder
     * @param group the leader group
     */
    private static void processLeaderGroup(JsonDocumentBuilder builder, String group) {
      // Get leader value
      String leaderValue = group.substring(group.indexOf(">") + 1, group.lastIndexOf("<"));

      // Create leader object
      JsonDocument leader = JsonDocument.builder()
          .withType(JsonType.OBJECT)
          .withField("value", JsonString.of(leaderValue))
          .build();

      // Add leader object to builder
      builder.withField("leader", leader);
    }

    /**
     * Processes a control field group.
     *
     * @param builder the JSON document builder
     * @param group the control field group
     */
    private static void processControlFieldGroup(JsonDocumentBuilder builder, String group) {
      // Get control field tag
      String controlFieldTag = group.substring(group.indexOf("tag=\"") + 5, group.indexOf("\">"));

      // Get control field value
      String controlFieldValue = group.substring(group.indexOf(">") + 1, group.lastIndexOf("<"));

      // Create control field object
      JsonDocument controlField = JsonDocument.builder()
          .withType(JsonType.OBJECT)
          .withField("tag", JsonString.of(controlFieldTag))
          .withField("value", JsonString.of(controlFieldValue))
          .build();

      // Add control field object to builder
      builder.withField("controlFields", controlField);
    }

    /**
     * Processes a data field group.
     *
     * @param builder the JSON document builder
     * @param group the data field group
     */
    private static void processDataFieldGroup(JsonDocumentBuilder builder, String group) {
      // Get data field tag
      String dataFieldTag = group.substring(group.indexOf("tag=\"") + 5, group.indexOf("\">"));

      // Get data field indicators
      String dataFieldIndicators = group.substring(group.indexOf(">") + 1, group.indexOf(" "));

      // Get data field subfields
      String dataFieldSubfields = group.substring(group.indexOf(" ") + 1, group.lastIndexOf("<"));

      // Create data field object
      JsonDocument dataField = JsonDocument.builder()
          .withType(JsonType.OBJECT)
          .withField("tag", JsonString.of(dataFieldTag))
          .withField("indicators", JsonString.of(dataFieldIndicators))
          .withField("subfields", processSubfields(dataFieldSubfields))
          .build();

      // Add data field object to builder
      builder.withField("dataFields", dataField);
    }

    /**
     * Processes subfields.
     *
     * @param subfields the subfields
     * @return the processed subfields
     */
    private static JsonDocument processSubfields(String subfields) {
      // Split subfields into groups
      List<String> subfieldGroups = Arrays.asList(subfields.split(MARC_XML_SUBFIELD_ELEMENT));

      // Create subfield object
      JsonDocument subfield = JsonDocument.builder()
          .withType(JsonType.OBJECT)
          .withField("code", JsonString.of(subfieldGroups.get(0).substring(group.indexOf("code=\"") + 6, group.indexOf("\">"))))
          .withField("value", JsonString.of(subfieldGroups.get(0).substring(group.indexOf(">") + 1, group.lastIndexOf("<"))))
          .build();

      // Add subfield object to builder
      builder.withField("subfields", subfield);

      // Return subfield object
      return subfield;
    }
  }
```