```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName mutatedClass = org.pitest.classinfo.ClassName.fromString(data.getMutatedClass());
    final byte[] classBytes = coverage.getClassBytes(mutatedClass);
    final long classId = coverage.getClassId(mutatedClass);
    final org.pitest.classinfo.ClassInfoBuilder classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, classId);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```