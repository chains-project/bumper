package se.kth.breaking_changes;

import java.lang.reflect.Modifier;
import java.util.Objects;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.experimental.Accessors;

@lombok.Setter
@lombok.Getter
@Accessors(chain = true)
public class ApiChange {
    private int oldModifier;
    private String oldReturnType;
    private String oldElement;
    
    private int newModifier;
    private String newReturnType;
    private String newElement;

    private String category;
    private String description;
    private String name;
    private ApiMetadata newVersion;
    private ApiMetadata oldVersion;

    public ApiChange() {
    }

    @Override
    public String toString() {
        ObjectMapper mapper = new ObjectMapper();
        try {
            return mapper.writeValueAsString(this);
        } catch (JsonProcessingException e) {
            return "";
        }
    }

    public String toDiffString() {
        if(!this.oldElement.equals("null")) {
            return "-- " + this.getCompleteValue();
        } else {
            return "++ " + this.getCompleteValue();
        }
    }

    public String getValue() {
        if(!this.oldElement.equals("null")) {
            return this.oldElement;
        } else {
            return this.newElement;
        }
    }

    public String getCompleteValue() {
        if(!this.oldElement.equals("null")) {
            return Modifier.toString(this.oldModifier) + " " + this.oldReturnType + " " + this.oldElement;
        } else {
            return Modifier.toString(this.newModifier) + " " + this.newReturnType + " " + this.newElement;
        }
    }

    public String getAction() {
        if(!this.oldElement.equals("null")) {
            return "REMOVE";
        } else {
            return "ADD";
        }
    }

    @Override
    public boolean equals(Object that) {
        if (this == that) return true;
        if (that == null || getClass() != that.getClass()) return false;
        ApiChange thatLibraryChange = (ApiChange) that;
        return this.oldElement.equals(thatLibraryChange.oldElement)
                && this.newElement.equals(thatLibraryChange.newElement)
                && this.category.equals(thatLibraryChange.category)
                && this.name.equals(thatLibraryChange.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(oldElement, newElement, category, name);
    }
}
