```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    java.util.Set<org.pitest.classinfo.ClassName> mutatedClassSet = java.util.Collections.singleton(data.getMutatedClass());
    java.util.Map<org.pitest.classinfo.ClassName, org.pitest.coverage.ClassInfo> classInfoMap = coverage.getClassInfo(mutatedClassSet);
    org.pitest.coverage.ClassInfo classInfo = classInfoMap.get(data.getMutatedClass());
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```