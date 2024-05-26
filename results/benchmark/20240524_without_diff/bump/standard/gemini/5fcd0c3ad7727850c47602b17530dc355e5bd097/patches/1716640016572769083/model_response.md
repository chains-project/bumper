```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final Set<org.pitest.classinfo.ClassName> classNames = new HashSet<>();
    classNames.add(data.getMutatedClass());
    final Map<org.pitest.classinfo.ClassName, org.pitest.coverage.ClassInfo> classInfos = coverage.getClassInfos(classNames);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfos.get(data.getMutatedClass()));
}
```