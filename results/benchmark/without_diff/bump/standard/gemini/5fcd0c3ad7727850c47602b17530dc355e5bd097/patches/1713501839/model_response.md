```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final Set<org.pitest.classinfo.ClassName> mutatedClass = Collections.singleton(data.getMutatedClass());
    final org.pitest.coverage.ClassInfo classInfo = coverage.getClassInfo(mutatedClass);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```