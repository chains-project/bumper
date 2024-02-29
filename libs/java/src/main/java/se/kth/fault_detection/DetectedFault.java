package se.kth.fault_detection;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import lombok.Getter;
import lombok.Setter;
import se.kth.log_Analyzer.MavenErrorLog;

@Setter
@Getter
@lombok.experimental.Accessors(chain = true)
public class DetectedFault {
    public String methodName;
    public String methodCode;
    public String inClassCode;
    public String plausibleDependencyIdentifier;
    public int clientLineNumber;
    public int clientEndLineNumber;
    public MavenErrorLog.ErrorInfo errorInfo;

    public DetectedFault() {
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

    public int getIdentifier() {
        return this.errorInfo.hashCode();
    }
}
