```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final java.util.Set<org.pitest.classinfo.ClassName> classes = java.util.Collections.singleton(data.getMutatedClass());
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), ++coverage.getCoverageDataForClasses(classes));
}
```