```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName className = org.pitest.classinfo.ClassName.fromString(data.getMutatedClass());
    final byte[] bytecode = data.getBytecode();
    final long time = data.getTime();
    final org.pitest.classinfo.ClassInfoVisitor visitor = new org.pitest.classinfo.ClassInfoVisitor();
    final org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = visitor.getClassInfo(className, bytecode, time);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
}
```