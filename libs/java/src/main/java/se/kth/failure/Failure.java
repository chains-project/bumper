package se.kth.failure;

import java.util.List;
import java.util.Set;
import se.kth.breaking_changes.ApiChange;
import se.kth.fault_detection.DetectedFault;

public class Failure {
    private Set<ApiChange> apiChanges;
    public DetectedFault detectedFault;

    public Failure(Set<ApiChange> apiChanges, DetectedFault detectedFault) {
        this.apiChanges = apiChanges;
        this.detectedFault = detectedFault;
    }

    public List<ApiChange> getApiChanges() {
        return this.apiChanges.stream()
            .sorted((a, b) -> {
                return a.getValue().compareTo(b.getValue());
            })
            .toList();
    }
}
