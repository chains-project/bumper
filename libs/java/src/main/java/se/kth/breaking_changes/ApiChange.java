package se.kth.breaking_changes;

import java.util.Objects;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class ApiChange {
    private String oldElement;

    private String newElement;

    private String category;

    private String description;

    private String name;

    private ApiMetadata newVersion;

    private ApiMetadata oldVersion;

    public ApiChange(String oldElement, String newElement, String category, String name) {
        this.oldElement = oldElement;
        this.newElement = newElement;
        this.category = category;
        this.name = name;

    }

    public ApiChange(String oldElement, String newElement, String category, String name, ApiMetadata newVersion, ApiMetadata oldVersion) {
        this.oldElement = oldElement;
        this.newElement = newElement;
        this.category = category;
        this.name = name;
        this.newVersion = newVersion;
        this.oldVersion = oldVersion;
    }

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
            return "-- " + this.oldElement;
        } else {
            return "++ " + this.newElement;
        }
    }

    public String getValue() {
        if(!this.oldElement.equals("null")) {
            return this.oldElement;
        } else {
            return this.newElement;
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
