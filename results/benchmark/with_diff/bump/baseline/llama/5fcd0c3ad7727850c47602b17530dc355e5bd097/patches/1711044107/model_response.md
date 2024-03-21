Here's a proposed patch to fix the failure:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a new ClassInfoBuilder with the class name and bytecode
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass().getName(), data.getMutatedClass().getBytes());
    // Use the ClassInfoBuilder to get the ClassInfo object
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    // Create a new MutationTestSummaryData object with the class info
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch creates a new `ClassInfoBuilder` object with the class name and bytecode, then uses it to get a `ClassInfo` object. The `ClassInfo` object is then passed to the `MutationTestSummaryData` constructor, along with the file name and mutations.

This patch uses the `ClassInfoBuilder` class, which is a new addition in the updated library version, to retrieve the `ClassInfo` object. It does not use the removed `getClassInfo` method from the `CoverageDatabase` class.