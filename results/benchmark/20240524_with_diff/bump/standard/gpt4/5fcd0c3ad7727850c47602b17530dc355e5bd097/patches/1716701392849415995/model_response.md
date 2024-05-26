```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = new org.pitest.classinfo.ClassInfoVisitor();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), builder.getClassInfo(data.getMutatedClass(), null, 0L));
}
```