```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final java.util.Set<org.pitest.classinfo.ClassName> mutatedClass = java.util.Collections.singleton(data.getMutatedClass());
    final java.util.Map<org.pitest.classinfo.ClassName, org.pitest.coverage.ClassInfo> classInfo = coverage.getClassInfos();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo.get(mutatedClass.iterator().next()));
}
```