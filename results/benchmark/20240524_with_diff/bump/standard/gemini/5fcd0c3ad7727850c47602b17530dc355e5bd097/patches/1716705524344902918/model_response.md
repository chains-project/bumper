```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassInfoBuilder builder = new org.pitest.classinfo.ClassInfoBuilder();
    coverage.visitClass(data.getMutatedClass(), builder);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), builder.build());
}
```