Here is a possible patch for the failing method:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    byte[] bytes = {}; // you may need to replace this with the actual bytecode of the class
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass().asString(), bytes, data.getMutatedClass().getBytes().length));
}
```

This patch uses the new `getClassInfo` method added to `ClassInfoVisitor` to create a `ClassInfo` object from the mutated class name and its bytecode. You may need to replace the `bytes` variable with the actual bytecode of the mutated class.