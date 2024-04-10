```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName mutatedClass = data.getMutatedClass();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), org.pitest.classinfo.ClassInfoVisitor.getClassInfo(mutatedClass, coverage.getClassBytecode(mutatedClass), coverage.getClassTimestamp(mutatedClass)));
}
```