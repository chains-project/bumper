Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass())));
}
```

Becomes:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), org.pitest.classinfo.ClassInfoBuilder.getClassInfo(data.getMutatedClass().getName(), coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()))));
}
```
The patch uses the `org.pitest.classinfo.ClassInfoBuilder` class to retrieve the `ClassInfo` object for the mutated class, since the `getClassInfo` method has been removed from the `CoverageDatabase` class.