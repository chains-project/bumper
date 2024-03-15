```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), data.getBytecode(), data.getMutationTimestamp());
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
}
```