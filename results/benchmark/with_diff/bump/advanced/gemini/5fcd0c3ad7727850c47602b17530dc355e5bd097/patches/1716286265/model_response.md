```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final Set<org.pitest.classinfo.ClassName> mutatedClass = Collections.singleton(data.getMutatedClass());
    final org.pitest.classinfo.ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    final byte[] classBytes = classInfo.getBytes();
    final long lastModifiedTime = classInfo.getLastModifiedTime();
    final org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), classBytes, lastModifiedTime);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
}
```