# dwarfy

Let's evaluate debugging user experience.
The tool automates the process of putting breakpoints and evaluating the quality of backtraces. At the moment, it supports only GDB, but I will add support for LLDB as well.

## Examples

### Process all functions of the program

	dwarfy-bt --process-entry-vals ./a.out
	== dwarfy ==
	version 1.0


	Do you want to specify functions for breakpoints? (y/n) n
	Are you sure you want to go through to all functions of the program? (y/n) y
	Please wait...

	Processing backtraces...

	====================================
	Num of backtraces proccessed 2
	<optimized out> parameters 16.67%
	@entry values 0.0%
	====================================

### Process just a function

	dwarfy-bt --process-entry-vals ./a.out
	== dwarfy ==
	version 1.0


	Do you want to specify functions for breakpoints? (y/n) y
	Please specify function to set breakpoint on it:
	fn2
	More functions? (y/n) n
	Processing backtraces...

	====================================
	Num of backtraces proccessed 1
	<optimized out> parameters 33.33%
	@entry values 0.0%
	====================================
