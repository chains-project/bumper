```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final Set<ClassName> mutatedClasses = Collections.singleton(data.getMutatedClass());
    final Map<ClassName, ClassInfo> classInfoMap = coverage.getClassInfos();
    final ClassInfo classInfo = classInfoMap.get(mutatedClasses.iterator().next());
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```