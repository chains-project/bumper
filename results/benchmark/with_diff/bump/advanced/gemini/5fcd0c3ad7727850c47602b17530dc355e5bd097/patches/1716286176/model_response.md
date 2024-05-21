```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName className = org.pitest.classinfo.ClassName.fromString(data.getMutatedClass());
    final byte[] classBytes = coverage.getClassByteCode(className);
    final long classTime = coverage.getClassTime(className);
    final org.pitest.classinfo.ClassInfo classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classBytes, classTime);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```