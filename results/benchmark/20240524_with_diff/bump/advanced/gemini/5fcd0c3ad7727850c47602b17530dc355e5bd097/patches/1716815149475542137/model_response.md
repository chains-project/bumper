```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName className = org.pitest.classinfo.ClassName.fromString(data.getMutatedClass());
    final byte[] bytecode = data.getFirstBytecode();
    final long time = data.getFirstTimestamp();
    final org.pitest.classinfo.ClassInfo classInfo = coverage.getClassInfoVisitor().getClassInfo(className, bytecode, time);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```