Here's a possible patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a new ClassInfoBuilder with the class name and bytecode
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass().getName(), data.getMutatedClass().getBytes());
    // Use the ClassInfoBuilder to get the ClassInfo object
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    // Create a new MutationTestSummaryData with the class info and mutations
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
This patch creates a new `ClassInfoBuilder` instance with the class name and bytecode, then uses it to get a `ClassInfo` object. The `ClassInfo` object is then passed to the `MutationTestSummaryData` constructor, along with the file name and mutations, to create a new `MutationTestSummaryData` instance.

This patch uses the `org.pitest.classinfo.ClassInfoBuilder` class, which is a new addition in the updated library version, to get the `ClassInfo` object. The `getClassInfo` method on the `CoverageDatabase` class is no longer available, so we need to use this alternative approach to get the `ClassInfo` object.

Note that this patch assumes that the `data.getMutatedClass()` method returns the class name and bytecode for the mutated class. If this method returns something different, the patch may need to be adjusted accordingly.