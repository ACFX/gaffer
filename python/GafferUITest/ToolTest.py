##########################################################################
#
#  Copyright (c) 2021, Cinesite VFX Ltd. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import unittest

import IECore

import Gaffer
import GafferTest
import GafferUI
import GafferUITest

class ToolTest( GafferUITest.TestCase ) :

	def testDerivingInPython( self ) :

		class TestTool( GafferUI.Tool ) :

			def __init__( self, view, name = "TestTool" ) :

				GafferUI.Tool.__init__( self, view, name )

		IECore.registerRunTimeTyped( TestTool, typeName = "GafferUITest::TestTool" )
		GafferUI.Tool.registerTool( "TestTool", GafferUITest.ViewTest.MyView, TestTool )

		self.assertIn( "TestTool", GafferUI.Tool.registeredTools( GafferUITest.ViewTest.MyView ) )

		view = GafferUITest.ViewTest.MyView()
		tool = GafferUI.Tool.create( "TestTool", view )
		self.assertIsInstance( tool, TestTool )
		self.assertIsInstance( tool, GafferUI.Tool )
		self.assertTrue( tool.view() is view )

		Gaffer.Metadata.registerValue( TestTool, "test", 10 )
		self.assertEqual( Gaffer.Metadata.value( tool, "test" ), 10 )

if __name__ == "__main__":
	unittest.main()
